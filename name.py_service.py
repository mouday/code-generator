# -*- coding: utf-8 -*-

from unittest import TestCase
from peewee_ext import to_dict
from typing import Dict


class Name.PyService:
    """name.py"""
    @classmethod
    def get_total(cls) -> int:
        return Name.PyModel.select().count()

    @classmethod
    @to_dict
    def get_row_by_id(cls, uid) -> Dict:
        return Name.PyModel.select().where(Name.PyModel.id == uid).first()


class TestName.PyService(TestCase):
    """test"""
    def test_get_total(self):
        ret = Name.PyService.get_total()
        print(ret)