from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming ....", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("La posicion es:", position)
    del todos[position]
    return jsonify(todos)


some_data = { "name": "Mimoun", "lastname": "El Yazidi" }
todos = [{ "label": "My first task", "done": False },]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)