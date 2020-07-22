# -*- coding: utf-8 -*-
"""All Blueprint objects and URL path names defined here.
"""
from flask import Blueprint


def _factory(view_module_path: str, blueprint_url_path: str):
    """Factory for generating blueprints imported in the view modules.

    :param view_module_path: represents module object referencing the view
        format of `parent.module`
    :type view_module_path: str

    :parameter blueprint_url_path: URL base pathname for the view.
    :type blueprint_url_path: str

    :return: a :class: `Blueprint` for a specific view module

    """
    name = view_module_path
    import_name = 'app.{}'.format(view_module_path)
    template_dir = 'templates'
    static_dir = 'static'
    blueprint = Blueprint(name,
                          import_name,
                          template_folder=template_dir,
                          static_folder=static_dir,
                          url_prefix=blueprint_url_path
                          )
    return blueprint


homepage_index = _factory('homepage.index', '/')
auth_user = _factory('auth.user', '/auth')
user_profile = _factory('user.profile', '/users')

application_blueprints = (homepage_index,
                          auth_user,
                          user_profile
                          )
