# -*- coding: utf-8 -*-
"""Tools for overloading dash objects."""

_custom_nav = """
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
"""
# fmt: off
_custom_index_str = (
    """
    <!DOCTYPE html>
    <html>
        <head>  
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="jumbotron rounded" style="padding-top:100px">
        """ + _custom_nav + """
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
)
# fmt: on
