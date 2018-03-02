FROM python:3

ENV PYTHONUNBUFFERED 1
RUN curl -so /usr/local/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod 777 /usr/local/wait-for-it.sh

RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN pip install pipenv --upgrade
## -- Adding Pipfiles
#COPY Pipfile Pipfile
#COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN pipenv install --deploy --system

# Collect our static media.
RUN python /app/manage.py collectstatic --noinput


CMD ["/bin/bash"]