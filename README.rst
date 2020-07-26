.. image:: https://travis-ci.org/CodeForPhilly/CHIME-2.svg?branch=master
    :target: https://travis-ci.org/CodeForPhilly/CHIME-2

=======
CHIME-2
=======

The folks over at Penn Medicine `have made improvements to the original model <https://help.ubuntu.com/community/Wubi>`_ To that end an upgrade
to the dashboard has been overdue. The purpose of this project is to create and updated platform to serve the new model.

Run Locally
-----------

You need Python and Node.js to run this.

Navigate to the directory.

To install the Python depends:

- with Pipenv ``pipenv install --dev``

- with Poetry ``poetry install --no-root``

Enter the venv shell

Install the node depends

- ``npm install``

Make a copy of the `env.example`

- ``cp .env.example .env``

Then set the env variables

- ``source .env``

Initialize the database

- ``flask db init``

- ``flask db migrate -m "Inital migration"``

- ``flask db upgrade``

You should be good to go. To run the app

- ``npm start``

You can ensure your code passes any QA checks by running

- ``flask lint --check``

- ``npm run lint``


[WIP]
