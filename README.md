# Courser Flow

**Courser Flow** é uma aplicação desktop desenvolvida em **Python** com interface gráfica  utilizando `customtkinter`, integrada a um sistema de inferência lógica em **Prolog** via `pyswip`.

O objetivo do projeto é auxiliar estudantes de Ciência da Computação da UFPB a planejarem seu fluxo acadêmico, verificando pré-requisitos e sugerindo automaticamente quais disciplinas podem ser cursadas.

---

## Funcionalidades

- **Seleção de Disciplinas Cursadas**  
  Interface organizada por períodos, onde o aluno marca as disciplinas já concluídas.

- **Verificação de Pré-requisitos**  
  Permite selecionar uma disciplina e verificar:
  - Se ela pode ser cursada
  - Quais pré-requisitos ainda faltam

- **Sugestão de Disciplinas**  
  Com base nas disciplinas já cursadas, o sistema lista automaticamente todas as disciplinas disponíveis para matrícula.

---

## Tecnologias Utilizadas

- **Python 3.10+** — Interface gráfica e integração com o motor lógico  
- **CustomTkinter** — Biblioteca Python para criar interfaces gráficas 
- **SWI-Prolog** — Motor de inferência lógica  
- **PySwip** — Ponte entre Python e Prolog  

---

## Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- Python 3  
- SWI-Prolog  

Download do SWI-Prolog: https://www.swi-prolog.org/Download.html  

> **Importante (Windows):** Durante a instalação, marque a opção para adicionar o SWI-Prolog ao **PATH**.

---

## Instalação

```bash
# Clonar o repositório
git clone https://github.com/Pedroqueiroz2/course-flow.git
# Entrar na pasta
cd course-flow

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
.\venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## ▶️ Execução
```bash
python interface.py
```
## Estrutura do projeto
```bash
├── interface.py        # Interface gráfica e integração com Prolog
├── regras.pl           # Base de conhecimento (disciplinas e pré-requisitos)
├── requirements.txt    # Dependências do projeto
```
## Como funciona

O sistema utiliza Programação Lógica para representar o fluxo do curso:

```prolog
pre_req/2                     % Define pré-requisitos
pode_cursar/2                 % Verifica se pode cursar
faltam_pre_requisitos/3       % Retorna o que falta
todas_podem/2                 % Lista disciplinas disponíveis
```


O Python atua como interface gráfica e envia consultas ao Prolog, que é responsável por toda a lógica de decisão.
