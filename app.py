#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import re
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

notes = [
	{
		"id" : 1,
		"body" : "Ask Larry about the TPS reports."
	}
]

# curl -i -H "Content-Type: application/json" -X POST -d '{"body" : "Pick up milk!"}' http://localhost/api/notes
# GET functions
@app.route('/api/notes', methods=['GET'])
def get_notes(): 		# Will return all elements in our collection or a specific note that matched our query
	if len(notes) == 0:
		return jsonify({'empty': 'There are currently no notes to retrieve'})
	if len(request.args) == 0:
		return jsonify(notes)
	else:
		queryRequest = request.args.get('query')
		note = [note for note in notes if re.search(queryRequest, note['body'], re.IGNORECASE) is not None]
		if len(note) == 0:
			abort(404)

		return jsonify(note)

@app.route('/api/notes/<int:note_id>', methods=['GET'])
def get_note(note_id): 	# will return a single element based on id value 
	note = [note for note in notes if note['id'] == note_id]
	if len(note) == 0:
		abort(404)

	return jsonify(note[0])

#POST functions
@app.route('/api/notes', methods=['POST'])
def create_note():
	if not request.json or not 'body' in request.json:
		abort(400)
	newId = 1

	if len(notes) != 0:
		newId = notes[-1]['id'] + 1 
	note = {
		'id': newId,
		'body': request.json.get('body', "") 
	}
	notes.append(note)
	return jsonify(note), 201

#PUT functions
@app.route('/api/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
	note = [note for note in notes if note['id'] == note_id]
	if len(note) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'body' in request.json and type(request.json['body']) is not unicode:
		abort(400)

	note[0]['body'] = request.json.get('body', note[0]['body'])

	return jsonify(note[0])

#DELETE functions
@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
	note = [note for note in notes if note['id'] == note_id]
	if len(note) == 0:
		abort(404)
	notes.remove(note[0])
	return jsonify({'result': True})

if __name__ == "__main__":
	app.run(debug=True)