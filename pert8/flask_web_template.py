#!flask/bin/python
from flask import Flask, request, render_template

app = Flask(__name__)

# Handle request GET ke alamat /
@app.route('/', methods=['GET'])
def index():
	# Render template yang ada di direktori 'templates' dengan parameter username
	return render_template('home.html', username="Bhawiyuga")

if __name__ == '__main__':
	app.run(debug=True, port=5001)