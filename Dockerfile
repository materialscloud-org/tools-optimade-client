FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir .

ENV BASE_PATH=/

EXPOSE 5000

CMD voila --base_url=${BASE_PATH} --Voila.ip=0.0.0.0 --port=5000 --no-browser --Voila.config_file_paths=./ OPTIMADE-Client.ipynb