#!/bin/bash

cd "$(dirname "$0")" && cd ..

docker run --env-file ./.env -it --memory="500m" awaken-email-service -p 5000:5000 