FROM python:3.12-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN pip install poetry  

RUN mkdir -p /app  
COPY . /app

WORKDIR /app

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

CMD ["bash", "start.sh"]