#!/bin/bash
#chmod u+x ./seed_database.sh
#./seed_database.sh


rm db.sqlite3
rm -rf ./lineupapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations lineupapi
python3 manage.py migrate lineupapi
python3 manage.py loaddata users
python3 manage.py loaddata lineup_token
python3 manage.py loaddata venues
python3 manage.py loaddata instruments
python3 manage.py loaddata profiles
python3 manage.py loaddata gigs



