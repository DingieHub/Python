FROM python:3-slim

RUN pip install python-bitvavo-api
RUN pip install redis

COPY bitvavoredis.py .

CMD ["python", "bitvavoredis.py"]