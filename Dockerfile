FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN pip install pipenv --upgrade
# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN pipenv install --deploy --system

ADD . /app/

CMD ["/bin/bash"]