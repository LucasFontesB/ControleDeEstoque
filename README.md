# Gerenciador de Estoque (Python + SQLite)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

Aplicativo desktop para controle de estoque direcionado a mercearias, mercados, disk e estabelecimentos que precisam de gerenciamento de inventário. Desenvolvido em Python com banco de dados SQLite, fornece visão de estoque, dashboard com métricas principais, login de usuário, relatórios de vendas e lucro, além de sistema de logs automáticos.

---

## 🔍 Descrição

O **Gerenciador de Estoque** é uma ferramenta simples e intuitiva para controlar produtos, acompanhar vendas e calcular lucros. Ao abrir o programa, o usuário é direcionado a um dashboard que exibe três dados essenciais. Recursos principais:

- **Visualização de Estoque**: listagem de produtos, quantidades disponíveis e alertas de baixa quantidade.
- **Dashboard Inicial**: exibe três indicadores-chave para o usuário ao abrir o sistema.
- **Sistema de Login**: autenticação de usuário com permissões para acesso às funcionalidades.
- **Relatório de Vendas**: histórico de vendas diárias e filtros por período.
- **Relatório de Lucro**: cálculo automático de lucro bruto/completo por produto ou por período.
- **Logs Automáticos**: todas as ações (login, inserção, atualização, venda) são registradas em arquivo de log com data e hora.

---

## 🚀 Tecnologias e Dependências Principais

- **Python 3.8+**  
- **SQLite3** (banco de dados leve, integrado ao Python)  
- **CustomTkinter** (interface gráfica moderna baseada em Tkinter)  
- **PIL / Pillow** (manipulação de imagens, ícones e recursos gráficos)  
- **Matplotlib** (geração de gráficos para relatório de lucros)  
- **logging** (registro automático de eventos em arquivo)  
- **datetime** (manipulação de datas e horários para relatórios e logs)

> O projeto foi desenvolvido usando **PyCharm** como IDE, mas você pode usar qualquer editor/IDE de sua preferência.

---

## 📦 Pré-requisitos

1. **Python 3.8 ou superior** instalado e configurado no `PATH`.  
2. **Git** (para clonar o repositório).  
3. As bibliotecas Python listadas abaixo (podem ser instaladas via `pip`):

   ```bash
   pip install customtkinter pillow matplotlib
As bibliotecas sqlite3, logging e datetime fazem parte da biblioteca padrão do Python, não exigem instalação adicional.

## ⚙️ Como instalar e executar
Clone este repositório

git clone https://github.com/LucasFontesB/gerenciador-estoque.git

cd gerenciador-estoque

Instale as dependências

Em um terminal/Prompt de Comando, execute:

pip install customtkinter pillow matplotlib

## Configuração Inicial

O banco de dados SQLite (estoque.db) será criado automaticamente ao executar o programa pela primeira vez.

Caso queira usar um arquivo de banco de dados pré-configurado, coloque-o na raiz do projeto com o nome estoque.db.

Execute o programa

python main.py

O sistema abrirá a tela de Login.

Usuário padrão (exemplo):

Usuário: admin
Senha: admin@123

Após login bem-sucedido, o Dashboard principal será exibido.

## 🏗 Estrutura do Projeto

main.py: inicializa a aplicação, configura janela principal e chama a tela de login.

database.py: gerencia a conexão SQLite e criação de tabelas (usuarios, produtos, vendas, logs).

Pasta ui/: contém todas as telas (GUI) construídas com CustomTkinter:

login.py: formulário de login.

Pasta models/: classes que representam entidades e realizam operações CRUD no banco:

usuario.py, produto.py, vendas.py, logs.py.

Pasta utils/: funções auxiliares e geração de gráficos (com matplotlib) para relatórios.

Pasta logs/: arquivo de log app.log é atualizado sempre que uma ação relevante é executada (login, inserção de produto, venda etc.).

## 🎯 Funcionalidades Principais
Login de Usuário.

Autenticação segura.

Dashboard Inicial

Exibe 3 indicadores que o usuário deve ver ao abrir o programa:

Quantidade total de itens em estoque.

Valor total de vendas no dia atual.

Lucro líquido acumulado no dia atual.

Visualização de Estoque

Tabela de produtos com colunas: ID, Nome, Categoria, Quantidade, Preço de Compra, Preço de Venda.

Botões para Adicionar, Editar e Excluir produtos.

Relatório de Vendas

Listagem de todas as vendas realizadas, com filtro por data (início/fim).

Relatório de Lucro

Cálculo automático de lucro bruto (preço de venda – preço de compra) por produto.

Relatório consolidado de lucro total por período.

Gráfico de barras (matplotlib) comparando lucro por categorias ou por produto.

Registro de Logs Automáticos

Todas as ações relevantes (login, criação/atualização/exclusão de produto, venda realizada) são registradas em logs/{Data e hora que aconteceu}.log com data, hora, usuário e descrição da ação.

Controle de erros e exceções capturados e registrados, facilitando debugs futuros.

## 🛠 Fluxo de Desenvolvimento
=== Criar/Atualizar Banco de Dados ===

Se precisar resetar: remova estoque.db e execute main.py para recriar tabelas automaticamente.

Para adicionar campos ou tabelas, edite database.py e ajuste as classes correspondentes em models/.

Adicionar Nova Tela (CustomTkinter)

Crie um novo arquivo .py em ui/, defina a classe com herança de customtkinter.CTkFrame ou CTkToplevel.

Adicione componentes (botões, labels, tabelas) no construtor e vincule eventos a funções em models/ ou utils/.

======

## 📫 Contato e Suporte
Autor: Lucas Fontes Britto

E-mail: lfontesbritto@gmail.com

Relatar Bugs/Requests: Abra uma issue neste repositório com detalhes do problema ou melhoria desejada.

Desenvolvido com ❤️ em Python para atender às necessidades de gerenciamento de estoque de pequenos comércios e mercearias.
Versão atual: 1.0.0 (Beta)
© 2025 Lucas Fontes Britto.
