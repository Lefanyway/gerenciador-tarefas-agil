Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade
- Sobre o Projeto
Este repositório simula o desenvolvimento de um Sistema de Gerenciamento de Tarefas para a empresa fictícia "TechFlow Solutions", especializada em soluções de software para logística. O objetivo principal é aplicar de forma prática os conceitos de Engenharia de Software, desde o planejamento ágil e versionamento de código até a implementação de funcionalidades, controle de qualidade com testes automatizados e gestão de mudanças.

O projeto foi construído utilizando Python, Streamlit e gerenciado no GitHub.

- Objetivo e Escopo
O sistema foi projetado para permitir que equipes de logística acompanhem o fluxo de trabalho em tempo real, priorizem tarefas críticas e monitorem o desempenho da equipe.

Foi feita a implementação de uma funcionalidade CRUD (Create, Read, Update, Delete) para o gerenciamento de tarefas, incluindo:

Criação de novas tarefas com título, descrição e nível de prioridade.

Leitura de todas as tarefas cadastradas em uma interface limpa.

Atualização do status de uma tarefa (A Fazer, Em Progresso, Concluído) e edição de seus detalhes.

Exclusão de tarefas.

Metodologia Ágil: Kanban
A metodologia ágil escolhida foi o Kanban, devido à sua simplicidade e foco no fluxo de trabalho visual, e Para a gestão das atividades, foi utilizado o GitHub Projects.

🚀 Como Executar o Projeto
Para executar este projeto localmente, siga os passos abaixo:

Clone o repositório:

Bash

git clone https://github.com/Lefanyway/gerenciador-tarefas-agil.git
cd gerenciador-tarefas-agil
Crie e ative um ambiente virtual:

Bash

# Crie o ambiente
python -m venv .venv
# Ative o ambiente (Windows)
.\.venv\Scripts\activate
# Ative o ambiente (Linux/macOS)
source .venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Execute a aplicação Streamlit:

Bash

streamlit run src/app.py
A aplicação abrirá automaticamente no seu navegador.


- Controle de Qualidade
Testes Automatizados
Utilizei a biblioteca PyTest para criar testes unitários que validam a lógica de negócio no módulo data_manager.py. Os testes garantem que as funcionalidades de adicionar, atualizar e deletar tarefas funcionam como esperado, independentemente da interface gráfica.

Integração Contínua com GitHub Actions
Foi configurado um pipeline de CI usando o GitHub Actions. A cada push para a branch main, o workflow é acionado para:


Configurar um ambiente Python limpo, instalar as dependências do projeto e executar a suíte de testes automatizados.


(Projeto de faculdade)