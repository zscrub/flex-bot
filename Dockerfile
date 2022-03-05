# syntax=docker/dockerfile:1
FROM python:3.10-slim

COPY interactions_bot.py /app
# COPY requirements.txt /app

WORKDIR ~/code/flex-bot

RUN python -m pip freeze > requirements.txt
# RUN python -m pip install -r requirements.txt

CMD ["python", "interactions_bot.py"]
