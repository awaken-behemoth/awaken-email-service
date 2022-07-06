FROM python:3.8.10


# copying api files to docker 
COPY ./api /api/

# copying project dependencies configuration to docker
COPY Pipfile /
COPY Pipfile.lock /

# copy of uswgi starter to dockerfile
COPY ./app.ini /

# docker starter script
COPY deploy.sh /


RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000

ENTRYPOINT ["./deploy.sh"]