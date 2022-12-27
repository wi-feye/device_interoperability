from src import app

import json
import time

from flask import request

import zdm

@app.route("/api/publish", methods=["POST"])
def publish():
    data = request.args.get("cred")
    print(request.data)
    return "ciao"