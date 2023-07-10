from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route("/")
def hello():
  return "Hello World!"
@app.route("/pp")
def home():
  return "BRUH!"
@app.route("/homie")
def home2():
  return render_template("homepage.html")
if __name__ == "__main__":
  app.run()