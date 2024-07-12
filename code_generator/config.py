# -*- coding: utf-8 -*-
from .generators.base_generator import BaseGenerator
from .generators.service_generator import ServiceGenerator
import os


def resolve_path(pathname):
    return os.path.join(os.getcwd(), pathname)


GENERATOR_MAP = {
    'base': BaseGenerator,
    'service': ServiceGenerator
}
