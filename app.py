import logging
from flask import Flask, request
import subprocess

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

PORT = 2222

@app.route('/')
def home():
    return "App Ready!"

@app.route('/run_script', methods=['POST'])
def run_script_linux():
    idletime = request.args.get('idletime')
    port_app = request.args.get('port')
    instanceid = request.args.get('instanceid')
    
    # Linux
    # result = subprocess.run(['./run_script.sh', idletime, port_app, instanceid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # WSL Windows + bash.exe
    result = subprocess.run(['bash.exe', './run_script.sh', idletime, port_app, instanceid], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

    pid = str(result.stdout.decode('utf-8').strip())

    if pid == 'server not started':
        response = {
            'status': 'failed'
        }, 500
    else:
        response = {
            'status': 'success',
            'pid': pid,
        }, 200

    return response

@app.route('/kill_script', methods=['POST'])
def kill_script_linux():
    pid = request.args.get('pid')

    # Linux
    # result = subprocess.run(['./kill_script.sh', pid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # WSL Windows + bash.exe
    result = subprocess.run(['bash.exe', './kill_script.sh', pid], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

    status = result.stdout.decode('utf-8').strip()

    return {'status': status}, 200


if __name__ == '__main__':
    app.run(port=PORT)