#!/bin/bash

source /home/alu5899/.virtualenvs/vm/bin/activate
uwsgi --ini /home/alu5899/webapps/vm/uwsgi.ini
