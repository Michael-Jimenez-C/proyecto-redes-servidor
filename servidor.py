from flask import Flask

app=Flask(__name__)

@app.route("/")
def main():
    return "<h1>ACTIVO</h1>"


app.run(host="0.0.0.0")