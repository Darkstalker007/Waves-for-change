from flask import Flask,render_template
from models import drive


drive1=drive('Mamzar Beach',2,'10:00 AM',True)
drive2=drive('Al Khan Beach',2.5,'11:00 AM',True)
drive3=drive('Kite Beach',3,'12:00 PM',False)


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
  return render_template('home.html',drives=DRIVES)

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True, port=2000)