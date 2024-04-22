from flask import Flask
## WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
  return "I am very much excited to learn flask"

@app.route('/newskill')
def newskill():
  return "Learning flask will help me in building end to end ML projects"

if __name__=='__main__':
  app.run(debug=True)