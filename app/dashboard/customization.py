# -*- coding: utf-8 -*-
"""
Dash app overloading

WIP:
"""
import dash

from app.dashboard.util import interpolate_str, load_html

nav_html = load_html("nav.html").split(
    "{% if current_user and current_user.is_authenticated %}"
)[0]
footer_html = load_html("footer.html")

custom_index_str = """<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        {%footer%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""


class CustomDash(dash.Dash):
    """Overloading the default methods for dash.Dash"""

    def interpolate_index(
        self,
        metas="",
        title="",
        css="",
        config="",
        scripts="",
        app_entry="",
        favicon="",
        renderer="",
        nav=nav_html,
        footer=footer_html,
    ):
        return interpolate_str(
            custom_index_str,
            metas=metas,
            title=title,
            nav=nav,
            css=css,
            config=config,
            scripts=scripts,
            footer=footer,
            favicon=favicon,
            renderer=renderer,
            app_entry=app_entry,
        )
