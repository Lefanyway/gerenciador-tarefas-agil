# tests/test_data_manager.py
from src import data_manager

def test_add_task():
    """Testa se a função add_task adiciona uma tarefa corretamente."""
    # Cenário: Começar com uma lista vazia
    tasks = []
    # Ação: Adicionar uma nova tarefa
    updated_tasks = data_manager.add_task(tasks, "Nova Tarefa", "Descrição Teste", "Média")
    # Verificação: A lista agora deve ter 1 item e os dados devem estar corretos
    assert len(updated_tasks) == 1
    assert updated_tasks[0]['titulo'] == "Nova Tarefa"
    assert updated_tasks[0]['status'] == "A Fazer"
    assert updated_tasks[0]['id'] == 1

def test_delete_task():
    """Testa se a função delete_task remove a tarefa correta."""
    # Cenário: Começar com uma lista com duas tarefas
    tasks = [
        {"id": 1, "titulo": "Tarefa 1", "descricao": "", "status": "A Fazer", "prioridade": "Alta"},
        {"id": 2, "titulo": "Tarefa 2", "descricao": "", "status": "A Fazer", "prioridade": "Baixa"}
    ]
    # Ação: Deletar a tarefa com id=1
    updated_tasks = data_manager.delete_task(tasks, 1)
    # Verificação: A lista deve ter apenas 1 item e deve ser a tarefa de id=2
    assert len(updated_tasks) == 1
    assert updated_tasks[0]['id'] == 2

def test_update_task_status():
    """Testa se a função de atualização de status funciona."""
    # Cenário: Uma tarefa com status "A Fazer"
    tasks = [{"id": 1, "titulo": "Tarefa Teste", "descricao": "", "status": "A Fazer", "prioridade": "Média"}]
    # Ação: Mudar o status para "Concluído"
    updated_tasks = data_manager.update_task_status(tasks, 1, "Concluído")
    # Verificação: O status da tarefa deve ser "Concluído"
    assert updated_tasks[0]['status'] == "Concluído"