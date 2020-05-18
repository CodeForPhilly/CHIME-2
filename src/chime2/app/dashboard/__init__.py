"""
Dashboard
=========

This dashboard was created using Plotly's Dash framework, which combines
flask and react to create interactive dashboards optimal for uses such
as this one. For specific information about Plotly Dash seek out their
documentation which is available `here. <https://dash.plot.ly>`_

The dashboard structure follows Model-View-Controller design pattern,
as well SOLID, YAGNI, and KISS design principles. For information
about MVC component please seek out the documentation in the respective
module.

---

Modules
~~~~~~~

callback:
    (controller) responsible for orchestrating interaction between model
    and view

component:
    (view) individual pieces of a page layout

page:
    dashboard layout defined here

process:
    (model) short-lived data manipulations which are triggered by
    callbacks

service:
    Run throughout the life of the dashboard
"""
