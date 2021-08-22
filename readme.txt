Events app

Intended to allow users to filter what's on by a selection of event types, cities and dates. The user selects their
event type, city and date from drop down lists on the web app and are presented with a list of events that meet
the requested criteria. This list will also display the number of likes and dislikes each event has. The user will be
able to click into their chosen event to get more information. The Details page will provide further details on the
event and also connect to the Google Maps API to display the location of the event venue.
(Connection-allowing,) the user will also be able to add their own likes or dislikes for the event if they have already
attended it in the past.

Features

- Web app with drop-down list to choose search criteria
- Results based on specified search criteria of event type, city and selected dates
- Results list includes likes and dislikes from other users for each event displayed
- More details page will also display the location of the event venue on Google Maps

Installation

Please download the code in your computer and follow the steps below (or equivalent instructions for your computer's
specifications) to create a virtual environment in the project folder*:


The websites below also have information about the steps to be followed:

https://flask.palletsprojects.com/en/2.0
https://realpython.com/flask-by-example-part-1-project-setup/

* You can also create the virtualenv and then download the project folder.

Steps:

1) Create a virtual environment:

virtualenv .env
or
py -3 -m venv venv

2) Activate the virtual environment

source .env/bin/activate
or
venv\Scripts\activate
or
you can just type activate after changing directory to the the Scripts or bin folder from the console if these don't
work.


3) Install the dependencies in the new virtual environment (not inside the venv folder, but on the same level as that
folder, right inside the events-app folder).

pip install -r requirements.txt


4) Choose which app you want flask to start with:

export FLASK_APP=main


5) Tell flask to start serving the app. You can copy and paste the server path in your browser if it doesn't
automatically start it. You can also click on the green run button to run main.py.

python -m flask run
