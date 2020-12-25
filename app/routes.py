from app import app
from app.utils.bout_observer import BoutObserver
from flask import request, jsonify


@app.route('/')
@app.route('/home')
def home():
    return "SBO HOMEPAGE"

@app.route('/restart')
def start():
    #if request.method == 'POST' and request.values.get('restart'):
    # bo.start_process()
    print(bo.c)
    return "PROCESS RESTART"

@app.route('/api/v1/status')
def api_v1_status():
    bo_json = {}
    bo_json['bout'] = bo.get_bout()
    bo_json['config'] = bo.c
    bo_json['process'] = bo.check_process()
    return jsonify(bo_json)

bo = BoutObserver()
bo.start_process()