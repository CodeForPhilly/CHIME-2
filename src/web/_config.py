"""
"""
import sys, os
import toml
from pathlib import Path
from collections import namedtuple
from dotenv import load_dotenv

__location__ = Path(os.getcwd()).absolute()
__dot_env__ = load_dotenv()
