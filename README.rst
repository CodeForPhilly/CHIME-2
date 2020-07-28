.. image:: https://travis-ci.org/CodeForPhilly/CHIME-2.svg?branch=master
    :target: https://travis-ci.org/CodeForPhilly/CHIME-2
    
=======
CHIME 2
=======

Next iteration of the Covid-19 Hospital Impact Model for Epidemics.


- ``/web`` Web application: 
  
  Node.js + Bootstrap 4 + Flask + Flask-WTF + Flask-Login + Overloaded Plotly-Dash

- ``/api`` Model API

  REST API serving the over the web interaction with ``chime2`` library.

- ``/chime2`` Python package
  
  pip installable Python package, for simplified use and integration of the normal approximations module from @ckoerber, as well as the original Penn Medicine model in other applications
