from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
@app.route("/")
def home2():
  return render_template("home.html")
@app.route("/form", methods =["GET"])
def home3():
  return render_template("form.html")

if __name__ == "__main__":
  app.run()