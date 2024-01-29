from flask import Flask, request
import subprocess, socket

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      return on_post()
   else:
      return on_get()

def on_post():
   subprocess.Popen(["python", "stress_cpu.py"])
   return "stress_cpu intialized"


def on_get():
   alias = socket.gethostname()
   ipAddress = socket.gethostbyname(alias)
   return str(ipAddress)

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')