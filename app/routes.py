from app import app
from app.utils.bout_observer import BoutObserver
from flask import request, jsonify, redirect


@app.route('/')
@app.route('/home')
def root():
    return redirect('/api/v1/status', code=302)


@app.route('/api/v1/help')
def api_v1_help():
    return jsonify(['/api/v1/help', '/api/v1/restart', '/api/v1/status', '/api/v1/terminate'])


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