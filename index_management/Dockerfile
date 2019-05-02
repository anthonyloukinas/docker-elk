FROM python:3

WORKDIR /app

COPY delete_indices.py /app

RUN pip install elasticsearch && \
    pip install elasticsearch-curator

CMD [ "python", "./delete_indices.py" ]
