# Building URL Dynamically
# Variable Rules and URL Building
# Integrating with HTML
'''
Jinja2 template engine
1. {% ... %} conditions,for statements
2. {{ }} expressions to print output
3. {# ... #} this is for comments
'''

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
  return render_template("index.html")

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
    exp={'score':average_score,'res':res}

    return render_template('result.html',result=exp)


if __name__=='__main__':
  app.run(debug=True)
