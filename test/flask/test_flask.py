#!/usr/bin/env python  
# -*- coding: utf-8  -*-
#time:'2018/4/30 下午 12:39'
#author:'jiayiming'
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hell():
    return "hello world!"

if __name__ == "__main__":
    app.run()