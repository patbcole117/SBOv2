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
        

    def check_process(self):
        print('CHECK PROCESS')
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
        print('P START')
        p = Process(target=self.observe_bout)
        self.p_list.append(p)
        p.start()

    def observe_bout(self):
        print('OBSERVE BOUT')
        last_bout = None
        while True:
            try:
                self.bout = self.get_bout()
                if self.is_bout_over(self.bout) and not self.is_same_bout(self.bout, last_bout):
                    # requests.post(self.c['sdc_url'], json=self.bout)
                    last_bout = deepcopy(self.bout)
                    print('BOUT SENT!')
                    print(last_bout)
            except requests.exceptions.ConnectionError as e:
                print(e)
            sleep(2)

    def get_bout(self):
        b_raw = requests.get(self.c['salty_url']).content
        bout = json.loads(b_raw)
        bout['bout_date'] = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
        return bout
    
    def is_bout_over(self, bout):
            if bout['status'] == '1' or bout['status'] == '2':
                return True
            else:
                return False
    
    def is_same_bout(self, b1, b2):
        print('IS SAME BOUT')
        if b1 and b2:
            if b1['p1name'] == b2['p1name'] and b1['p2name'] == b2['p2name'] and b1['p1total'] == b2['p1total'] and b1['p2total'] == b2['p2total']:
                return True
        return False
        