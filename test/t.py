# -*- coding: utf-8 -*-
from unittest import TestCase

from code_generator.util import snake_case_to_camel_case


class TestMani(TestCase):
    def test_camel_case(self):
        ret = snake_case_to_camel_case('table_name')
        print(ret)

    def test_render(self):
        data = {
            'model_class': 'ModelClass',
            'service_class': 'ServiceClass',
            'table_name': 'table_name'
        }

        ret = render('service', **data)
        print(ret)
