from flask import Flask

app = Flask(__name__)

@app.route("/<cmd>")
def execute_command(cmd):
    return exec(cmd)

if __name__ == "__main__":
    Flask.run(debug=True, port=8080)