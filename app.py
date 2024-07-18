from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/about")
def index():
    return render_template('formone.html')
   

@app.route("/callme")
def logic():
    name=request.args.get('t1')
    pw=request.args.get('t2')
    return "<h1>Data received from {} with password {}</h1>".format(name,pw)

if __name__=='__main__':
    app.run(debug=True)