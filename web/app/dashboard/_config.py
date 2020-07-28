# -*- coding: utf-8 -*-
"""dashboard/_config.

Dashboard specific configuration settings.
"""
from app.config import CONF_DIR
from app.util import load_json

PARAMETER_META = load_json(CONF_DIR + "/model-parameters.json")
