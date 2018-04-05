#!flask/bin/python
from flask import Flask, request

app = Flask(__name__)

main_html = "<html><body>%s</body></html>"

# Handle request GET ke alamat /
@app.route('/', methods=['GET'])
def index():
	return main_html % "Hello, World!"

# Handle request GET ke alamat /user
@app.route('/user', methods=['GET'])
def user():
	try :
		# Ambil parameter dengan key "username"
		username = request.args["username"]
	except KeyError :
		username = ""
	return main_html % "Username anda adalah : "+username

# Handle request GET ke alamat /form
@app.route('/form', methods=['GET'])
def get_form():
	return '<html><body><form method="POST"><input name="data" type="text" /> <input type="submit" value="Submit" /></form></body></html>'

# Handle request POST ke alamat /form
@app.route('/form', methods=['POST'])
def post_form():
	# Ambil parameter dengan key "data"
	return '<html><body>You submitted: %s</body></html>' % request.form.get('data')

if __name__ == '__main__':
	app.run(debug=True, port=5000)