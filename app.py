from flask import Flask,render_template
from models import drives


drive1=drives('Mamzar Beach',2,'10:00 AM',True)
drive2=drives('Al Khan Beach',2.5,'11:00 AM',True)
drive3=drives('Kite Beach',3,'12:00 PM',False)


DRIVES_1=[drive1,drive2,drive3]

DRIVES=[
  {
    'id':1,
    'destination':'Mamzar Beach',
    'duration': 2,
    'time':'10:00 AM',
    'active':True,
  },
  {
    'id':2,
    'destination':'Al Khan Beach',
    'duration': 2.5,
    'time':'11:00 AM',
    'active':True,
  },
  {
    'id':1,
    'destination':'Kite Beach',
    'duration': 3,
    'time':'12:00 PM',
    'active':False,
  },
]

app=Flask(__name__)
@app.route("/")
def hello():
  return render_template('home.html',drives=DRIVES_1)

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True, port=2000)