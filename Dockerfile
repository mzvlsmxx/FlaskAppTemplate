FROM python:3.13-alpine3.22
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk update && \
    apk upgrade musl
RUN mkdir flask_app_template
COPY ./requirements.txt flask_app_template/requirements.txt
RUN pip install -r flask_app_template/requirements.txt
COPY . /flask_app_template
WORKDIR /flask_app_template
ENTRYPOINT ["python3", "main.py"]