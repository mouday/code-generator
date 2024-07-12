# -*- coding: utf-8 -*-
import os
from abc import ABC

from jinja2 import Template

from code_generator.logger import logger
from code_generator.util import resolve_template


class BaseGenerator(ABC):
    """
    input + data => output
    """
    default_prefix = ''
    default_suffix = ''
    default_template_dir = 'templates'
    default_template = 'base'
    default_template_ext = '.tpl'

    def __init__(self,
                 name: str,
                 template: str = None,
                 template_dir=None,
                 template_ext=None,
                 output_dir: str = '',
                 prefix: str = '',
                 suffix: str = '',
                 force: bool = False,
                 **kwargs):
        self.name = name

        self.output_dir = output_dir
        self.force = force

        self.template_dir = template_dir or self.default_template_dir
        self.template = template or self.default_template
        self.template_ext = template_ext or self.default_template_ext
        self.prefix = prefix or self.default_prefix
        self.suffix = suffix or self.default_suffix

        self.kwargs = kwargs

    def get_output_name(self):
        return os.path.join(self.output_dir, self.prefix + self.name + self.suffix)

    def generate(self):
        output_name = self.get_output_name()
        output_content = self.render()

        if os.path.exists(output_name) and not self.force:
            logger.error('file exists: %s', output_name)
            return False

        with open(output_name, 'w') as f:
            f.write(output_content)

        logger.debug('output file: %s', output_name)

        return True

    def get_template_data(self):
        return {'name': self.name}

    def get_template_name(self):
        template = self.template

        if not template.endswith(self.template_ext):
            template += self.template_ext

        if os.path.exists(template):
            return template

        elif os.path.exists(os.path.join(self.template_dir, template)):
            return os.path.join(self.template_dir, template)

        else:
            return resolve_template(template)

    def get_template_source(self):
        template = self.get_template_name()
        logger.debug('template: %s', template)

        with open(template, 'r') as f:
            return f.read()

    def render(self):
        source = self.get_template_source()
        data = self.get_template_data()

        template = Template(source=source)

        return template.render(**self.kwargs, **data)
