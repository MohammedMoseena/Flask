# Building URL Dynamically
# Variable Rules and URL Building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
  return "Welcome to Result Checker"

@app.route('/success/<int:score>')
def success(score):
  return "Congratulations you have passed your test with score:"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
  return "Ohh noo you have failed your test with score:"+str(score)

@app.route('/results/<int:marks>')
def results(marks):
  result=''
  if marks<50:
    result='fail'
  else:
    result='success'
  return redirect(url_for(result,score=marks))


if __name__=='__main__':
  app.run(debug=True)
