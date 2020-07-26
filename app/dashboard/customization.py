# -*- coding: utf-8 -*-
"""Tools for overloading dash objects.

WIP:
"""
import dash

from app.dashboard.util import interpolate_str, load_html

nav_html = load_html("nav.html").split(
    "{% if current_user and current_user.is_authenticated %}"
)[0]
footer_html = load_html("footer.html")

custom_index_str = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <div class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <a class="navbar-brand" href="https://www.pennmedicine.org/">
            <img class="container"
                 src="https://www.pennmedicine.org/Assets/PennMedicine/built/images/assets/logo-white.svg">
        </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="/">CHIME 2
                        <span class="sr-only">(current)</span>
                    </a>
                </li>
                <!--Secondary navbar links -->
                <li class="nav-item">
                    <a class="nav-link" href="/dashboard/">Dashboard</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/contributors/">Contributors</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/about/">Guide</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/about/">About</a>
                </li>
            </ul>
        </div>
    </div>
    <body class="jumbotron rounded" style="padding-top:100px">
    <h1 class="display-4 mx-auto" style="text-align:center">THIS IS A TEST SERVER</h1>
    {%app_entry%}
    <footer>
        {%config%}
        {%scripts%}
        {%renderer%}
    </footer>
    </body>
</html>
"""


class CustomDash(dash.Dash):
    """Overloaded custom ``Dash`` class."""

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
        """Overloads the default base html template."""
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
