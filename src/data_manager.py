# src/data_manager.py
import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def load_data():
    """Carrega as tarefas do arquivo JSON."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(tasks):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, titulo, descricao, prioridade):
    """Adiciona uma nova tarefa à lista e retorna a lista atualizada."""
    if not tasks:
        next_id = 1
    else:
        next_id = max(task['id'] for task in tasks) + 1

    new_task = {
        "id": next_id,
        "titulo": titulo,
        "descricao": descricao,
        "status": "A Fazer",
        "prioridade": prioridade
    }
    tasks.append(new_task)
    return tasks

def delete_task(tasks, task_id):
    """Deleta uma tarefa pelo ID e retorna a lista atualizada."""
    return [t for t in tasks if t['id'] != task_id]

def update_task_status(tasks, task_id, new_status):
    """Atualiza o status de uma tarefa."""
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
    return tasks