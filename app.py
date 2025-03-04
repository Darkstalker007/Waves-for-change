from flask import Flask,render_template,jsonify
from database import load_drives,load_drive



app=Flask(__name__)
@app.route("/")
def hello():
  DRIVES = load_drives()
  return render_template('home.html',drives=DRIVES)

@app.route("/drive/<drive_id>")
def show_drive(drive_id):
  return render_template('drive.html',drive=load_drive(drive_id))


if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True, port=2000)