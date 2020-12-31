from app.utils.conf_parse import get_config
from copy import deepcopy
from datetime import datetime
from multiprocessing import Process
from time import sleep

import json
import requests


class BoutObserver:
    def __init__(self):
        print('CREATE BOUT OBSERVER')
        self.bout = ""
        self.c = get_config()
        self.p_list = []

    # Bout observing
    def bout_alert(self):
        if self.is_bout_open():
            alert_list = self.c["alert_list"]
            print(alert_list)

    def get_bout(self):
        b_raw = requests.get(self.c['salty_url']).content
        try:
            bout = json.loads(b_raw)
            bout['bout_date'] = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
            return bout
        except json.decoder.JSONDecodeError as e:
            print(e)
            return None

    def is_bout_open(self):
        if self.bout:
            if self.bout['status'] == 'open':
                return True
        return False

    def is_bout_over(self):
        if self.bout:
            if self.bout['status'] == '1' or self.bout['status'] == '2':
                return True
        return False
    
    def is_same_bout(self, b1, b2):
        if b1 and b2:
            if b1['p1name'] == b2['p1name'] and b1['p2name'] == b2['p2name'] and b1['p1total'] == b2['p1total'] and b1['p2total'] == b2['p2total'] and b1["status"] == b2["status"]:
                return True
        return False

    def observe_bout(self):
        print('OBSERVE BOUT')
        # the last bout does not exist
        last_bout = None
        while True:
            try:
                # retrieve current bout informatioon from saltybet
                self.bout = self.get_bout()
                # if the last bout is different from the current bout: send out alerts and make set the last bout to the current bout
                if not self.is_same_bout(self.bout, last_bout):
                    self.bout_alert()
                    last_bout = deepcopy(self.bout)
                    print(last_bout)
                    # if the current bout is over send the match results to the SDC to be recorded.
                    if self.is_bout_over():
                        requests.post(self.c['sdc_url'], json=self.bout)
                        print("sent")
            except requests.exceptions.ConnectionError as e:
                print(e)
            sleep(2)

    # Process management
    def check_process(self):
        if len(self.p_list) == 1:
            if self.p_list[0].exitcode == None:
                return True
        return False

    def terminate_process(self):
        for p in self.p_list:
            print('P TERMINATE')
            p.kill()
            p.join()
            p.close()
        self.p_list.clear()

    def start_process(self):
        self.terminate_process()
        p = Process(target=self.observe_bout)
        self.p_list.append(p)
        p.start()
