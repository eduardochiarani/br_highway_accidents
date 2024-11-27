# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de dependências para o container
COPY requirements.txt ./

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do projeto para o container
COPY . .

# Exponha a porta que será usada pelo Streamlit
EXPOSE 8501

# Comando para rodar a aplicação
CMD ["streamlit", "run", "src/dashboard.py", "--server.port=8501", "--server.enableCORS=false"]
