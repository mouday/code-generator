# -*- coding: utf-8 -*-

from code_generator.generators.base_generator import BaseGenerator
from ..util import snake_case_to_camel_case, resolve_template


class ServiceGenerator(BaseGenerator):
    default_template = 'service'
    default_suffix = '_service.py'

    def get_template_data(self):
        camel_name = snake_case_to_camel_case(self.name)

        data = {
            'camel_name': camel_name,
            'name': self.name
        }

        return data
