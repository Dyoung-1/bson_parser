#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import json
from bson import json_util
from flask import Flask 
from flask import request
from flask import render_template

app = Flask(__name__)

def parse_bson(content):
    pretty_content = json.dumps(content, default=json_util.default, indent=4)
    return pretty_content

@app.route('/', methods=['GET'])
def get():
    print request
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    return 'POST'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
