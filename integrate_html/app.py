# Building URL Dynamically
# Variable Rules and URL Building

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
  return render_template("index.html")

@app.route('/success/<int:score>')
def success(score):
  return render_template("success.html",result=score)

@app.route('/fail/<int:score>')
def fail(score):
  return render_template("fail.html",result=score)

### Result Checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
  average_score=0
  if request.method=='POST':
    science=float(request.form['science'])
    math=float(request.form['math'])
    c=float(request.form['c'])
    data_science=float(request.form['datascience'])
    average_score=(science+math+c+data_science)/4
    res=''
    if average_score<50:
      res='fail'
    else:
      res='success'

    return redirect(url_for(res,score=average_score))


if __name__=='__main__':
  app.run(debug=True)
