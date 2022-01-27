from flask import Flask, render_template
from random import randrange
from os import environ as env

app = Flask(__name__)
healthy = True


def update_health():
    global healthy
    if randrange(10) == 7:
        healthy = False
    return healthy


@app.route("/")
def hello_world():
    if update_health():
        return render_template("index.html", pod_name=env.get("POD_NAME", "somewhere"))


@app.route("/healthz")
def healthz():
    if update_health():
        return "OK"
