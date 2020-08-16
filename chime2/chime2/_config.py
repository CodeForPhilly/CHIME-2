# -*- coding: utf-8 -*-
"""Package configuration and settings.

Library configuration and settings actions should remain explicitly
upstream from initialization.
"""
import os
import sys
import datetime as dt
from pathlib import Path
from collections import namedtuple

HOME = str(Path.home())  # Get platform agnostic user root


def _mk_output_dir(directory_path: str = HOME):
    dir_tree = {"chime2": ["output", "figures", "parameters",]}
    if "CHIME_DIR" in os.environ:
        dir_path = os.environ["CHIME_DIR"]
    elif directory_path == HOME:
        dir_path = HOME + "/chime2"
    else:
        dir_path = directory_path
    if Path(dir_path).exists():
        print(f"'{dir_path}' already exists, skipping.")
    else:
        os.makedirs(dir_path)
        for sub_directory in dir_tree["chime2"]:
            os.makedirs(os.path.join(dir_path, sub_directory))
    os.environ["CHIME_DIR"] = dir_path


def _infer_output_directory():
    """Determine the output directory"""

    # Check if environment variable currently set
    if "CHIME_DIR" not in os.environ:
        # Inform user that the environment variable is not currently set
        print("CHIME_DIR not set please specify an output directory.")
        # Check if user wishes to use default path
        use_default = input("Use default? [y/n]: ")

        if use_default.lower() in ["y", "yes"]:
            # Use default args to create directory
            _mk_output_dir()
            # Remind user to set environment variable in the future
            print(f"You should set CHIME_DIR={os.environ['CHIME_DIR']}")

        elif use_default.lower() in ["n", "no"]:
            # Make output directory using user args
            user_selection = input("Specify a path for the output directory: ")
            if user_selection:
                _mk_output_dir(directory_path=user_selection)
                # Remind user to set environment variable
                print(f"You should set CHIME_DIR={user_selection}.")

        # Recurse if invalid selection
        else:
            _infer_output_directory()
    else:
        # Covers edge-case where user reads documentation
        _mk_output_dir(directory_path=os.environ["CHIME_DIR"])


class Config:
    """Configuration object."""

    def __init__(self):
        if "CHIME_DIR" not in os.environ:
            _infer_output_directory()
        self.OUTPUT_DIRECTORY = os.environ["CHIME_DIR"]
