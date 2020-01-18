from flask import Flask, Response, request, jsonify
import json
from db import DB

app = Flask(__name__)
db = DB()

@app.route('/<resource_name>/<resource_id>', methods = ['GET', 'POST', 'DELETE'])
def routeFunction(resource_name, resource_id):
    if request.method == 'GET':
        result = db.findResource(resource_name, resource_id)
        if result:
            return jsonify(result), 200
        else:
            return Response("Not found", status=404, mimetype='application/json')

    elif request.method == 'POST':
        db.saveResource(resource_name, resource_id, request.json)
        return Response("Created", status=201, mimetype='application/json')

    elif request.method == 'DELETE':
        db.deleteResource(resource_name, resource_id)
        return Response("Deleted", status=204, mimetype='application/json')

    else:
        return Response("No such functionality", status=404, mimetype='application/json')

@app.route('/')
def hello():
    return Response("Hello Python-Flask!")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')