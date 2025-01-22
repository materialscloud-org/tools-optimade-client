FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install .

EXPOSE 5000

CMD ["voila", "--Voila.ip=0.0.0.0", "--port=5000", "--no-browser", "--Voila.config_file_paths=./", "OPTIMADE-Client.ipynb"]
