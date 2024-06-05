FROM python:3.10-slim

WORKDIR .

COPY app.py .

RUN pip install flask waitress

EXPOSE 7777

CMD ["python", "app.py"]
