from flask import Flask,render_template
from models import drives


drive1=drives('Mamzar Beach',2,'10:00 AM',True)
drive2=drives('Al Khan Beach',2.5,'11:00 AM',True)
drive3=drives('Kite Beach',3,'12:00 PM',False)


DRIVES=[drive1,drive2,drive3]


app=Flask(__name__)
@app.route("/")
def hello():
  return render_template('home.html',drives=DRIVES)

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True, port=2000)