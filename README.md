# Miðhraun

## Setting up environment for development
1. Install pip
    * sudo apt-get install python-pip
2. Setup virtualenv for python
    * sudo apt-get install python-virtualenv
    * virtualenv .
3. Setup python requirements
    * source bin/activate
    * pip instal -r requirements.txt
    * python manage.py migrate

run `deactivate` in order to fix up system paths once you want to stop development

## Running the server
1. source bin/activate
2. python manage.py runserver
    * optionally run `manage.py <localhost>:<port>` to start the server on a port different than the default 8000
