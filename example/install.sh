#!/bin/bash

# break on any error
set -e

# creates a virtualenv
virtualenv --no-site-packages VEGETARIANCOOKBOOK
source VEGETARIANCOOKBOOK/bin/activate

pip install -r ../requirements.txt

if [ ! -d ./vegetarian_cookbook ]; then
    echo "\nSymlinking vegetarian_cookbook into this app directory:"
    ln -s ../vegetarian_cookbook/ ./vegetarian_cookbook
fi

echo
echo "Creating a sqllite database:"
./manage.py migrate

echo
echo "Compiling messages:"
./manage.py compilemessages > /dev/null

echo
echo "to activate the virtualenv:"
echo "source VEGETARIANCOOKBOOK/bin/activate"

echo
echo 'to create an admin account:'
echo './manage.py createsuperuser'

echo
echo "to run the testserver:"
echo "./manage.py runserver"
echo
echo "then open this url:"
echo "http://127.0.0.1:8000/admin/"
echo
echo "to close the virtualenv or just close the shell:"
echo "deactivate"

exit 0
