FROM python:3.10.8
ARG CONFIG=config.PrdConfig
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8
ENV FLASK_CONFIG $CONFIG

CMD python -m gunicorn -w 4 --timeout 600 -b 0.0.0.0:5000 "app:create_app()"