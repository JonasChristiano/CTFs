#!/usr/bin/env python3

from flask import Flask, render_template, request
from subprocess import run
app = Flask(__name__)

@app.route("/", methods=["POST", 'GET'])
def hello():
  output=None
  if request.method == 'POST' and (cmd := request.form['f']):
    output = run(f"type {cmd}", shell=True,
      capture_output=True).stdout.decode("utf-8")
    return cmd + "\n" + output
  else:
    return render_template("cmd0.html", output=output)

@app.route("/robots.txt")
def hellwo():
  return "Opa! Parece que você tá procurando no lugar errado :v"

if __name__ == "__main__":
    app.run()