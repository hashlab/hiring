FROM python:3.8.1-slim

RUN pip install pipenv==2020.11.15

WORKDIR /app

COPY Pipfile Pipfile.lock .
RUN pipenv install --system --deploy

COPY app/ .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000" ]
