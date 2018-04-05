from flask import Flask, abort
import json

app = Flask(__name__)

list_node = [{"id": 1, "temp": 37, "humdity" : 70},
			{"id": 2, "temp": 40, "humdity" : 80}]


@app.route('/node', methods=['GET'])
def semua():
	return json.dumps(list_node)

@app.route('/node/<int:node_id>', methods=['GET'])
def satu(node_id):
	node = None
	for n in list_node :
		if n["id"] == node_id :
			node = n
	if node :
		return json.dumps(node)
	else :
		abort(404)

if __name__=='__main__':
	app.run(debug=True, port=7777)	