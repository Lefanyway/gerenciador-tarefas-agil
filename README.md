# ✅ Gerenciador de Tarefas Ágil com GitHub

## 📌 Sobre o projeto

O projeto é **Sistema de Gerenciamento de Tarefas** para a empresa fictícia **TechFlow Solutions**, aplicando conceitos reais de **Engenharia de Software**:

* Planejamento ágil
* Controle de versão
* Implementação de funcionalidades
* Testes automatizados
* Gestão de mudanças

A aplicação foi desenvolvida em **Python + Streamlit**, com todo o ciclo de vida controlado no **GitHub**.

---

## 🎯 Objetivo do Sistema

Auxiliar equipes de **logística** a:

* Acompanhar o fluxo de trabalho
* Priorizar tarefas
* Monitorar desempenho em tempo real

---

## 🔧 Funcionalidades (CRUD Completo)

| Ação          | Descrição                                                                  |
| ------------- | -------------------------------------------------------------------------- |
| **Criar**     | Adicionar tarefa com título, descrição e prioridade                        |
| **Ler**       | Visualizar todas as tarefas em interface simples                           |
| **Atualizar** | Alterar status (`A Fazer`, `Em Progresso`, `Concluído`) ou editar detalhes |
| **Excluir**   | Remover tarefas do sistema                                                 |

---

## 📌 Metodologia Ágil

Metodologia adotada: **Kanban**

Justificativa:

* Simples
* Visual
* Foco no fluxo contínuo

Ferramenta utilizada: **GitHub Projects (aba “Projects”)**

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar repositório

```bash
git clone https://github.com/Lefanyway/gerenciador-tarefas-agil.git
cd gerenciador-tarefas-agil
```

### 2️⃣ Criar e ativar ambiente virtual

```bash
# Criar ambiente
python -m venv .venv

# Ativar (Windows)
.\.venv\Scripts\activate

# Ativar (Linux/macOS)
source .venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar aplicação

```bash
streamlit run src/app.py
```

A aplicação abrirá automaticamente no navegador.

---

## ✅ Garantia de Qualidade

### 🔹 Testes Automatizados (PyTest)

Testes unitários verificam:

* Adição de tarefas
* Atualização de status
* Exclusão de registros


### 🔹 Integração Contínua (GitHub Actions)

Pipeline acionado a cada `push` na branch `main`:

1. Cria ambiente Python limpo
2. Instala dependências
3. Executa testes automatizados

