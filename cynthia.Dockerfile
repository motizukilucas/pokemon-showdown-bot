FROM python:3.11

WORKDIR /app

COPY cynthia .

RUN pip3 install poke-env python-dotenv tensorflow-cpu

CMD python3 cynthia
