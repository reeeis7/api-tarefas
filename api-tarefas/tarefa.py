class Tarefa:

    def __init__(self, task_id, titulo, descricao, status, prioridade, categoria, dataConclusao):

        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.categoria = categoria
        self.dataConclusao = dataConclusao

    def to_json(self):
        return{
            "task_id": self.task_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "prioridade": self.prioridade,
            "categoria": self.categoria,
            "dataConclusao": self.dataConclusao
        }