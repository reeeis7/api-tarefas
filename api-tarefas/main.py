from flask import Flask, request, jsonify
from flasgger import Swagger
from tarefa import Tarefa

app = Flask(__name__)
swagger = Swagger(app)

tarefas = [
    Tarefa(
        task_id=1,
        titulo="Estudar js",
        descricao= "Estudar para aprender a construir eventos",
        status= "Em andamento",
        prioridade="Alta",
        categoria="Estudos",
        dataConclusao="2024-06-30").to_json(),
    Tarefa(
        task_id=2,
        titulo="Arrumar a casa",
        descricao="Arrumar a casa para a proxima tarefa",
        status="Nao iniciado",
        prioridade="Media",
        categoria="Casa",
        dataConclusao="2024-06-20").to_json(),
    Tarefa(
        task_id=3,
        titulo="Praticar HTML e CSS",
        descricao="Criar um layout responsivo para melhorar habilidades",
        status="Nao iniciado",
        prioridade="Media",
        categoria="Desenvolvimento Web",
        dataConclusao="2024-07-15").to_json()
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Retorna todas as tarefas
    ---
    responses:
      200:
        description: Lista de tarefas
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              titulo:
                type: string
              descricao:
                type: string
              status:
                type: string
              prioridade:
                type: string
              dataConclusao:
                type: string
              categoria:
                type: string
    """
    return jsonify(tarefas)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    """
    Retorna uma tarefa pelo ID
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa
    responses:
      200:
        description: Tarefa encontrada
        schema:
          type: object
          properties:
            id:
              type: integer
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            prioridade:
              type: string
            dataConclusao:
              type: string
            categoria:
              type: string
      404:
        description: Tarefa não encontrada
    """
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            return jsonify(tarefa)
    return jsonify({"error": "Tarefa não encontrada"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Cria uma nova tarefa
    ---
    parameters:
      - name: task
        in: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            prioridade:
              type: string
            dataConclusao:
              type: string
            categoria:
              type: string
    responses:
      201:
        description: Tarefa criada com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            prioridade:
              type: string
            dataConclusao:
              type: string
            categoria:
              type: string
    """
    task = request.json
    ultimo_id = tarefas[-1].get('task_id') + 1 if tarefas else 1
    task['task_id'] = ultimo_id
    tarefas.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Atualiza uma tarefa existente
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa a ser atualizada
      - name: task
        in: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            prioridade:
              type: string
            dataConclusao:
              type: string
            categoria:
              type: string
    responses:
      200:
        description: Tarefa atualizada com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            prioridade:
              type: string
            dataConclusao:
              type: string
            categoria:
              type: string
      404:
        description: Tarefa não encontrada
    """
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            task_search = tarefa
            break

    if not task_search:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo', task_search.get('titulo'))
    task_search['descricao'] = task_body.get('descricao', task_search.get('descricao'))
    task_search['status'] = task_body.get('status', task_search.get('status'))
    task_search['prioridade'] = task_body.get('prioridade', task_search.get('prioridade'))
    task_search['dataConclusao'] = task_body.get('dataConclusao', task_search.get('dataConclusao'))
    task_search['categoria'] = task_body.get('categoria', task_search.get('categoria'))

    return jsonify(task_search)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Exclui uma tarefa
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa a ser excluída
    responses:
      200:
        description: Tarefa excluída com sucesso
      404:
        description: Tarefa não encontrada
    """
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            tarefas.remove(tarefa)
            return jsonify({"message": "Tarefa excluída"}), 200
    return jsonify({"error": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
