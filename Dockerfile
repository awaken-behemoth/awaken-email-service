FROM python:3.8.10


COPY ./api /api/
COPY Pipfile /
COPY .env /
COPY Pipfile.lock /
COPY prod.sh /

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

RUN pipenv install

ENTRYPOINT ["./prod.sh"]