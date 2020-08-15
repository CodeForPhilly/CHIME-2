# -*- coding: utf-8 -*-
"""Main package interface.

All interactions with the package should be managed from this single api
instance which itself handles the logic required to access the various
implementations of the model. The purpose of this is two-fold; first,
this allows for friendlier user interaction, second it is beneficial to
project iteration as new components or modules can be developed and
worked on without explicitly affecting usability of the library.
"""


class Sim(object):
    pass
