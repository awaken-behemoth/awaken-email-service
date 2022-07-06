#!/bin/bash

cd "$(dirname "$0")" && cd ..

uwsgi app.ini