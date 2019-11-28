
from flask import Flask, jsonify, render_template, request
import webbrowser
#from qr import *
import time

app = Flask(__name__)

"""@app.route('/_stuff', methods = ['GET'])
def stuff():
        
    return jsonify(result='1234.jpg')
"""

@app.route('/')
def index():
   
    return render_template('dy1.html')

    
if __name__ == '__main__':
    
    app.run()
