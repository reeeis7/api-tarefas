from flask import Flask, request, render_template


app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar js",
        "descricao": "Estudar para aprender a construir eventos",
        "status": "Em andamento",
        "prioridade": "Alta",
        "dataConclusao": "2024-06-30",
        "categoria": "Estudos"
    },
    {
        "id": 2,
        "titulo": "Arrumar a casa",
        "descricao": "Arrumar a casa para a proxima tarefa",
        "status": "Nao iniciado",
        "prioridade": "Media",
        "dataConclusao": "2024-06-20",
        "categoria": "Casa"
    },
    {
        "id": 3,
        "titulo": "Fazer compras",
        "descricao": "Comprar mantimentos para a semana",
        "status": "Pendente",
        "prioridade": "Alta",
        "dataConclusao": "2024-06-15",
        "categoria": "Compras"
    },
    {
        "id": 4,
        "titulo": "Academia",
        "descricao": "Treinar pernas e bracos",
        "status": "Em andamento",
        "prioridade": "Baixa",
        "dataConclusao": "2024-06-25",
        "categoria": "Saude"
    },
    {
        "id": 5,
        "titulo": "Ler um livro",
        "descricao": "Terminar a leitura do livro atual",
        "status": "Pendente",
        "prioridade": "Media",
        "dataConclusao": "2024-07-01",
        "categoria": "Lazer"
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa

    return 'Tarefa não encontrada'

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa
    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['prioridade'] = task_body.get('prioridade')
    task_search['dataClonclusao'] = task_body.get('dataClonclusao')
    task_search['categoria'] = task_body.get('categoria')

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
    return 'excluída'




if __name__ == '__main__':
    app.run(debug=True)