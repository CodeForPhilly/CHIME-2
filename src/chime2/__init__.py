#! /usr/env/python3
"""
.. currentmodule:: chime2-app

chime2
======

Reactive web application presenting the latest iteration of the Covid-19
Hospital Impact Model for Epidemics from the Predictive Healthcare team
at Penn Medicine. Built using the flask and dash libraries this app aims
to provide an insightful user experience for those seeking to gain
insights from the advanced epidemiological modeling techniques created
by data scientists at the nation's first hospital system and academy.

----

The chime2 application uses the
`bayes_chime <https://www.github.com/pennsignals/chime_sims/tree/master/bayes_chime>`_
normal extension, created by Dr. Chris Koerber of UC Berkley, which
optimizes for speed the latest CHIME iteration by assuming normal
distributions among model parameters. Thanks to his work, and the work
of the Penn Medicine team we can offer this application.

"""
__all__ = []
__version__ = "2.0.0.dev0"
