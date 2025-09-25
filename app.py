from flask import Flask,render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
        
'''
git init
git add .
git commit -m "iitial"
git remote add origin "your repo name url"
git push -u origin master
'''
