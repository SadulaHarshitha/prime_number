from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def input():
  return render_template(input.html)
  
if __name__ == '__main__'
    app.run(debud=True)
