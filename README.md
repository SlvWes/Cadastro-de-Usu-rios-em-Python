# Sistema de Cadastro de Usuários em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Funcionando-green)

Este projeto é uma aplicação de linha de comando em Python que permite cadastrar usuários, armazenando nome, email e CPF em arquivos `.txt`. Possui um menu interativo colorido, tornando a experiência mais intuitiva e agradável no terminal. É ideal para quem deseja praticar Python, manipulação de arquivos e criação de menus interativos simples.

## ✨ Funcionalidades

- ✅ **Cadastrar novos usuários** - Armazena nome, email e CPF
- ✅ **Listar todos os usuários** - Visualiza todos os cadastros realizados
- ✅ **Menu interativo colorido** - Interface amigável com cores no terminal
- ✅ **Validação de entradas** - Verificação básica de dados inseridos
- ✅ **Armazenamento persistente** - Dados salvos em arquivo TXT
- ✅ **Opção de saída** - Encerramento controlado do sistema

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação principal
- **Colorama** - Biblioteca para adicionar cores ao terminal
- **Arquivos TXT** - Armazenamento simples e eficiente de dados

## 🚀 Como Usar

1. Execute o sistema:
```bash
python cadastro.py
```

2. No menu interativo, escolha uma das opções:
   - **1** - Cadastrar novo usuário
   - **2** - Listar todos os usuários
   - **3** - Sair do sistema

3. Siga as instruções para cadastrar usuários ou visualizar os cadastros existentes.

## 📁 Estrutura do Projeto

```
sistema-cadastro-python/
├── cadastro.py    # Código principal do sistema
├── Nome.txt           # Arquivo de armazenamento de dados (gerado automaticamente)
├── Email.txt
└── CPF.txt
```

## 📸 Demonstração

### 1. Cadastrando usuário
![Cadastro de Usuário](https://github.com/user-attachments/assets/341fb2f1-b61e-416b-9044-88578909db0d)

### 2. Lista de usuários
![Lista de Usuários](https://github.com/user-attachments/assets/e370ea6d-5fa4-4123-b2bf-7669e5f59ea2)

### 3. Saindo do sistema
![Saindo do Sistema](https://github.com/user-attachments/assets/bde77f02-85b4-432c-8de4-6c414cc54bbc)

### 4. Opção inválida
![Opção Inválida](https://github.com/user-attachments/assets/e79e17a6-e37b-4e88-970f-9c0e8889a334)

## 🔧 Personalização

Você pode personalizar o sistema editando as cores no arquivo `sistema_cadastro.py`:

```python
# Cores disponíveis
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
```

## 📞 Contato

Email - wesley.s.rezende2006@gmail.com
Numero - 11987993250

---

**Desenvolvido com Python e Colorama**
