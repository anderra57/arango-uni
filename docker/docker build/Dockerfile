FROM python:3.7-alpine
EXPOSE 5000

COPY *.py /app/
COPY requirements.txt /app/
COPY MOCK_DATA_MARKS.json /app/
COPY /static/* /app/static/
COPY /templates/* /app/templates/

WORKDIR /app/

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk -q update && apk -q add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt