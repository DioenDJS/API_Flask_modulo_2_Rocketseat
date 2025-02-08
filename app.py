from flask import Flask, request, jsonify
from typing_task import TaskTyping
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
    return jsonify({"message":"Nova tarefa criada com suucesso", "id": new_task.id})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }

    return jsonify(output)

@app.route('/tasks/<id>', methods=['GET'])
def get_task(id:str):
    for t in tasks:
        if t.id == id:
            return t.to_dict()

    return jsonify({"message": "Mão foi possível encontrar a atividade "}), 404

@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    task:TaskTyping = None
    for t in tasks:
        if t.id == str(id):
            task = t
            break

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()

    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    return jsonify({"message":"Tarefa atualizada com sucesso"})

@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = None

    for t in tasks:
        if t.id == str(id):
            task = t
            break

    if not task:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)