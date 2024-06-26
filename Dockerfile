FROM python:3.9.16-alpine3.16

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80


ENTRYPOINT [ "python3", "entry_point.py"]