# -*- coding: utf-8 -*-
from code_generator.version import VERSION
from .generators.base_generator import BaseGenerator
from .logger import logger
from .config import GENERATOR_MAP
from .cli import parse_args


def main():
    params = parse_args()

    logger.debug(params)

    generator_name = params.pop('generator')
    if generator_name in GENERATOR_MAP:
        generator = GENERATOR_MAP[generator_name]
    else:
        params['template'] = generator_name
        generator = BaseGenerator

    gen = generator(**params)
    gen.generate()


if __name__ == '__main__':
    main()
