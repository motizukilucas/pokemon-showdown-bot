FROM python:3.11

WORKDIR /app

COPY ash.py .

RUN pip3 install poke-env python-dotenv

CMD python3 ash.py
