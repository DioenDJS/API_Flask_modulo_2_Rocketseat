from flask import Flask, request, jsonify
from models.task import Task
import uuid


app = Flask(__name__)

tasks = []
task_id_control = 1
@app.route("/")
def hello_word():
    return "Hello Word!"

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(id=str(uuid.uuid4()), title=data['title'], description=data.get("description", ""))
    tasks.append(new_task)
    return jsonify({"mesage":"Nova tarefa criada com suucesso"})

if __name__ == "__main__":
    app.run(debug=True)