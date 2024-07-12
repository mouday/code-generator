# -*- coding: utf-8 -*-
from unittest import TestCase

from code_generator.generators.service_generator import ServiceGenerator


class TestServiceGenerator(TestCase):
    def setUp(self) -> None:
        self.generator = ServiceGenerator('table_name')

    def test_get_template_data(self):
        template_data = self.generator.get_template_data()
        print(template_data)

    def test_generate(self):
        ret = self.generator.generate()
        print(ret)
