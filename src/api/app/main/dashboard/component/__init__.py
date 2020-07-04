# -*- coding: utf-8 -*-
"""
==========
Components
==========

Components define individual views of the application. A component may
consist of sub-components, but a page is never a component. Components
derive from a base class Component which defines a setter and getter
for the individual dash components of which it consists.

Language settings and parameters are now decoupled from the application
view. Default settings should be defined in configuration files and
statically generated.

Contents
--------

base:
    Base class for components.

text:
    Contains class for reading in static text templates.

navbar:
    Contains class for initializing the navigation bar.

"""
