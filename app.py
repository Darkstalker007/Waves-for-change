from flask import Flask,render_template
from database import load_drives



app=Flask(__name__)
@app.route("/")
def hello():
  DRIVES = load_drives()
  return render_template('home.html',drives=DRIVES)

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True, port=2000)