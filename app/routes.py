from app import app
from app.utils.bout_observer import BoutObserver
from flask import request, jsonify, redirect


@app.route('/')
@app.route('/home')
def root():
    return redirect('/api/v1/status', code=302)


@app.route('/api/v1/help')
def api_v1_help():
    help = {}
    help['/api/v1/help'] = 'Display avalible URLs and descriptions.'
    help['/api/v1/restart'] = 'Terminate running bout_observer processes (if any) and start a new one.'
    help['/api/v1/status'] = 'Display config.txt information, process state, and real-time bout information.'
    help['/api/v1/terminate'] = 'Terminate running bout_observer processes.'
    return jsonify(help)


@app.route('/api/v1/restart')
def api_v1_restart():
    bo.start_process()
    return 'PROCESS RESTART!'


@app.route('/api/v1/status')
def api_v1_status():
    bo_json = {}
    bo_json['bout'] = bo.get_bout()
    bo_json['config'] = bo.c
    bo_json['process'] = bo.check_process()
    return jsonify(bo_json)


@app.route('/api/v1/terminate')
def api_v1_terminate():
    bo.terminate_process()
    return 'PROCESS TERMINATED!'


bo = BoutObserver()
bo.start_process()