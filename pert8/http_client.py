import httplib, urllib

conn = httplib.HTTPConnection("localhost:5000")

def get_index():
	# Kirim request GET ke url /
	conn.request("GET", "/")
	# Baca response
	response = conn.getresponse()
	resp = response.read()
	# Print response
	print resp

def get_user():	
	params = urllib.urlencode({'username': 'Bhawiyuga'})
	conn.request("GET", "/user?%s" % (params))
	response = conn.getresponse()
	resp = response.read()
	print resp

def post_form():	
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	params = urllib.urlencode({'data': 'helloooooo'})
	conn.request("POST", "/form", params, headers)
	response = conn.getresponse()
	resp = response.read()
	print resp

get_index()
#post_form()
#get_user()