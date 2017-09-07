. ../env/bin/activate
cd ../app/
pip install -r requirements/prod.txt  | grep -v 'Requirement already satisfied' | grep -v 'Cleaning up...'
./manage.py collectstatic --noinput --clear
./manage.py migrate -v 0
circusctl reload
