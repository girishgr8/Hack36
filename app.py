from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup
import os

# Creating instance of Flask...
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route("/", methods=['POST', 'GET'])
def index():
	return render_template('safeRoutes.html')

if __name__ == "__main__":
# debug=True helps to render changes of website without need for running the server again & again....
	app.run(debug=True)


'''

To run the Flask Application on Windows Platform :-

Point to Flask App file => set FLASK_APP=app.py
Set Flask Environment to Development mode => set FLASK_ENV=development
Run the Flask App => flask run
Flask app url => http://127.0.0.1:5000/ 

'''