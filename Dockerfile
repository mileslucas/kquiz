FROM python:3

ENV PYTHONUNBUFFERED 1
RUN pip install pipenv --upgrade
## -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN pipenv install --deploy --system

COPY docker-entrypoint.sh /usr/local/docker-entrypoint.sh
RUN chmod +x /usr/local/docker-entrypoint.sh
RUN mkdir /app
ADD . /app
WORKDIR /app

ENTRYPOINT ["/usr/local/docker-entrypoint.sh"]
CMD ["/bin/bash"]
