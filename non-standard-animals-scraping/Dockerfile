FROM python:3.9.6-slim-buster
COPY requirements.txt requirements.txt
COPY app.py app.py
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "run"]
EXPOSE 5000
