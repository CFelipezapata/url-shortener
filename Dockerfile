FROM python:3.8.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

RUN mkdir /urlshortener

WORKDIR /urlshortener

COPY ./urlshortener /urlshortener

RUN pip install -r requirements.txt