#import flask,render_template
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
  #render_template
  return render_template('home.html')

  

