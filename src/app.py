# src/app.py
import streamlit as st
import data_manager

st.set_page_config(page_title="Gerenciador de Tarefas Ágil", page_icon="🚀")

# --- INICIALIZAÇÃO DO ESTADO ---
if 'tasks' not in st.session_state:
    st.session_state.tasks = data_manager.load_data()

# --- UI ---
st.title("Gerenciador de Tarefas - TechFlow Solutions 🚀")

with st.expander("➕ Adicionar Nova Tarefa", expanded=False):
    with st.form(key="add_task_form", clear_on_submit=True):
        new_titulo = st.text_input("Título da Tarefa")
        new_descricao = st.text_area("Descrição (Opcional)")
        new_prioridade = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"])

        if st.form_submit_button(label="Adicionar Tarefa"):
            if new_titulo:
                st.session_state.tasks = data_manager.add_task(st.session_state.tasks, new_titulo, new_descricao, new_prioridade)
                data_manager.save_data(st.session_state.tasks)
                st.success(f"Tarefa '{new_titulo}' adicionada!")
                st.rerun()

st.divider()
st.header("📋 Lista de Tarefas")

# ... (O restante do código de exibição e edição continua o mesmo) ...
if not st.session_state.tasks:
    st.info("Nenhuma tarefa cadastrada.")
else:
    prioridade_colors = {"Alta": "red", "Média": "orange", "Baixa": "green"}
    for task in sorted(st.session_state.tasks, key=lambda x: x['id'], reverse=True):
        with st.container(border=True):
            col1, col2 = st.columns([4, 1.5])
            with col1:
                st.markdown(f"**{task['titulo']}**")
                st.markdown(f"<span style='color:{prioridade_colors[task['prioridade']]}'>Prioridade {task['prioridade']}</span>", unsafe_allow_html=True)
                if task['descricao']:
                    st.caption(task['descricao'])

            with col2:
                status_options = ["A Fazer", "Em Progresso", "Concluído"]
                current_status_index = status_options.index(task['status'])
                new_status = st.selectbox("Status", status_options, index=current_status_index, key=f"status_{task['id']}", label_visibility="collapsed")
                if new_status != task['status']:
                    st.session_state.tasks = data_manager.update_task_status(st.session_state.tasks, task['id'], new_status)
                    data_manager.save_data(st.session_state.tasks)
                    st.rerun()

            action_col1, action_col2 = st.columns([1, 1])
            if action_col1.button("✏️ Editar", key=f"edit_{task['id']}", use_container_width=True):
                st.session_state.editing_task_id = task['id']
            if action_col2.button("🗑️ Excluir", key=f"delete_{task['id']}", type="primary", use_container_width=True):
                st.session_state.tasks = data_manager.delete_task(st.session_state.tasks, task['id'])
                data_manager.save_data(st.session_state.tasks)
                st.rerun()

# --- LÓGICA DO FORMULÁRIO DE EDIÇÃO ---
if 'editing_task_id' in st.session_state and st.session_state.editing_task_id is not None:
    task_to_edit = next((task for task in st.session_state.tasks if task['id'] == st.session_state.editing_task_id), None)

    if task_to_edit:
        with st.expander(f"✏️ Editando: {task_to_edit['titulo']}", expanded=True):
            with st.form(key="edit_form"):
                edited_titulo = st.text_input("Título", value=task_to_edit['titulo'])
                edited_descricao = st.text_area("Descrição", value=task_to_edit['descricao'])
                prioridades = ["Alta", "Média", "Baixa"]
                edited_prioridade = st.selectbox("Prioridade", prioridades, index=prioridades.index(task_to_edit['prioridade']))

                save_col, cancel_col = st.columns(2)
                if save_col.form_submit_button("Salvar Alterações", use_container_width=True, type="primary"):
                    task_to_edit['titulo'] = edited_titulo
                    task_to_edit['descricao'] = edited_descricao
                    task_to_edit['prioridade'] = edited_prioridade
                    data_manager.save_data(st.session_state.tasks)
                    st.session_state.editing_task_id = None
                    st.success("Tarefa atualizada!")
                    st.rerun()

                if cancel_col.form_submit_button("Cancelar", use_container_width=True):
                    st.session_state.editing_task_id = None
                    st.rerun()