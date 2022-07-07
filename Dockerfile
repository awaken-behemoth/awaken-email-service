FROM python:3.8.10

# create new user
RUN useradd -ms /bin/bash awaken

USER awaken
WORKDIR /home/awaken
ENV PATH="/home/awaken/.local/bin:$PATH"

#updating pip
RUN python -m pip install --upgrade pip --disable-pip-version-check

# copying api files to docker 
COPY ./api ./api

# copying project dependencies configuration to docker
COPY Pipfile ./
COPY Pipfile.lock ./

# copy of uswgi starter to dockerfile
COPY ./app.ini ./

# docker starter script
COPY cmd ./cmd

RUN cd api && cd ..
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 3001

ENTRYPOINT ["uwsgi", "/home/awaken/app.ini"]