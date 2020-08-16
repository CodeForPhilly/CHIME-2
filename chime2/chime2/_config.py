# -*- coding: utf-8 -*-
"""Package configuration and settings.

Library configuration and settings actions should remain explicitly
upstream from initialization.
"""
import sys, os
import datetime as dt
from pathlib import Path
from collections import namedtuple

HOME = str(Path.home())


def _mk_output_dir(directory_path: str=HOME):
    dir_tree = {
        "chime2": [
            "output",
            "figures",
            "parameters",
        ]
    }
    env_var = os.environ['CHIME_DIR']
    out_root = env_var if env_var is not None else 'chime2'
    chime_dir = os.path.join(directory_path, str(out_root))
    if Path(chime_dir).exists():
        print(f"'{chime_dir}' already exists, skipping.")
        return chime_dir
    os.makedirs(chime_dir)
    for sub_directory in dir_tree['chime2']:
        os.makedirs(os.path.join(chime_dir, sub_directory))
    return chime_dir


def _infer_output_directory():
    """Determine the output directory"""
    if 'CHIME_DIR' not in os.environ:
        print('CHIME_DIR not set please specify an output directory.')
        use_default = input('Use default? [y/n]: ')
        if use_default.lower() in ['y', 'yes']:
            chime_dir = _mk_output_dir()
            if chime_dir:
                print(f"You should set CHIME_DIR={chime_dir}")
        elif use_default.lower() in ['n', 'no']:
            chime_dir = input("Specify a path for the output directory: ")
            new_out_dir = _mk_output_dir(directory_path=chime_dir)
            if new_out_dir:
                print(f"You should set CHIME_DIR={chime_dir}.")
        else:
            _infer_output_directory()
        return chime_dir
    else:
        return _mk_output_dir(directory_path=os.environ["CHIME_DIR"])


OUT_DIR = _infer_output_directory()


