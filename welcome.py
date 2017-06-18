# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, request, json, render_template, jsonify
from random import sample
from datetime import datetime

app = Flask(__name__)
global val, time
val = [0]
time = [str(datetime.now())]

@app.route('/')
def index():
    return render_template('graphing.html')

@app.route('/data')
def data():
    global val
    global time
    print val, time
    return jsonify({'val' : val, 'time' : time})

@app.route('/stop_update')
def stop():
    global val
    global time
    val = [0]
    time = [str(datetime.now())]
    return jsonify({'val' : val, 'time' : time})

@app.route('/receiveData/', methods = ['POST', 'GET'])
def receiveData():
    global val, time
    jsondata = request.get_json(force=True)
    print "DEBUG1: ", jsondata
    # d = json.loads(jsondata)['Data']
    d = jsondata['Data']
    print "DEBUG2: ", d
    val.append(int(d))
    time.append(str(datetime.now()))
    result = {'escalate': True}
    return json.dumps(result)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
