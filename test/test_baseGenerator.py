# -*- coding: utf-8 -*-
from unittest import TestCase

from code_generator.generators.base_generator import BaseGenerator


class TestBaseGenerator(TestCase):

    def setUp(self) -> None:
        self.generator = BaseGenerator('table_name')

    def test_get_output_name(self):
        output_name = self.generator.get_output_name()
        print(output_name)

    def test_generate(self):
        ret = self.generator.generate()
        print(ret)

    def test_get_template_data(self):
        template_data = self.generator.get_template_data()
        print(template_data)

    def test_get_template_source(self):
        template_source = self.generator.get_template_source()
        print(template_source)

    def test_render(self):
        ret = self.generator.render()
        print(ret)

