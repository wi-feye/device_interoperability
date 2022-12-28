from src import app

import json
from datetime import datetime
import time
import os

from flask import request

import zdm

@app.route("/api/publish", methods=["POST"])
def publish():
    data = json.loads(request.data)
    cred = data['cred']
    payload = data['payload']
    tag = data['tag']

    # connecting to Zerynth Cloud
    print(cred)
    credential = zdm.Credentials(cred)
    device = zdm.ZDMClient(credential)
    device.connect()    

    # sending payload to Zerynth Cloud
    device.publish(payload, tag)
    time.sleep(5)

    return {"status" : True}