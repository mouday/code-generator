# -*- coding: utf-8 -*-

from unittest import TestCase
from peewee_ext import to_dict
from typing import Dict


class NameService:
    """name"""
    @classmethod
    def get_total(cls) -> int:
        return NameModel.select().count()

    @classmethod
    @to_dict
    def get_row_by_id(cls, uid) -> Dict:
        return NameModel.select().where(NameModel.id == uid).first()


class TestNameService(TestCase):
    """test"""
    def test_get_total(self):
        ret = NameService.get_total()
        print(ret)