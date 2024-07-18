from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    langs=['java','python','cobol','C','html']
    return render_template('home.html',langs=langs)





if __name__=='__main__':
    app.run(debug=True)