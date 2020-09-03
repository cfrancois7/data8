FROM python
LABEL maintainer="C.Francois"

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN apt update \
&& apt upgrade && pip install -r requirements.txt

COPY ./ /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]