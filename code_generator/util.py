# -*- coding: utf-8 -*-
import argparse

import os

from code_generator.version import VERSION


def resolve_path(pathname):
    return os.path.join(os.getcwd(), pathname)


def resolve_template(filename, dirname='templates'):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), dirname, filename)


def snake_case_to_camel_case(name: str):
    """
    table_name -> TableName
    :param name:
    :return:
    """
    return ''.join([char.title() for char in name.split('_')])



