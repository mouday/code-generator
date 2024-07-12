# -*- coding: utf-8 -*-

from unittest import TestCase
from peewee_ext import to_dict
from typing import Dict


class {{camel_name}}Service:
    """{{name}}"""
    @classmethod
    def get_total(cls) -> int:
        return {{camel_name}}Model.select().count()

    @classmethod
    @to_dict
    def get_row_by_id(cls, uid) -> Dict:
        return {{camel_name}}Model.select().where({{camel_name}}Model.id == uid).first()


class Test{{camel_name}}Service(TestCase):
    """test"""
    def test_get_total(self):
        ret = {{camel_name}}Service.get_total()
        print(ret)