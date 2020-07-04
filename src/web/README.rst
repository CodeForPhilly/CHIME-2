=====================
CHIME-2 Web Dashboard
=====================

Welcome to the CHIME-2 project.


Run CHIME-2 Locally
~~~~~~~~~~~~~~~~~~~

Place the following in a ``.env`` file.

.. code-block::

    export FLASK_APP=run
    export FLASK_ENV=development
    export DATABASE_URL=sqlite:///$PWD/app.db
    export SECRET_KEY=precious_secret_key


run ``source .env``

