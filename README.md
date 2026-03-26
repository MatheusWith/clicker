# Clicker Automation 🤖

Automação baseada em RPA para processamento de documentos, gestão de estoque e login automatizado utilizando Python e PyAutoGUI.

## 🚀 Como rodar o projeto

Siga os passos abaixo para configurar e executar o bot em sua máquina.

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado em seu sistema.

### 2. Adicione as imagens
Adicione as dentro de img/

### 3. Instalação de Dependências
O projeto utiliza as bibliotecas `pyautogui` para controle de periféricos e `python-dotenv` para variáveis de ambiente. Para que o reconhecimento de imagem (`confidence`) funcione, o `opencv-python` também é necessário.

Com o uv 
```bash
uv run main.py
```

Sem o uv
Crie a venv
```bash
python -m venv .venv
```

Inicie a venv e ative-a
```bash
python -m venv .venv
source venv/bin/activate
```
Instale as dependedncias
```bash
pip install -r requirements.txt
```
Execute
```bash
python  main.py
```
