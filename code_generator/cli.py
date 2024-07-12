# -*- coding: utf-8 -*-
import argparse

from code_generator.version import VERSION


def get_version():
    return 'code-gen version:' + VERSION


def parse_args():
    """
    支持不定的关键字参数
    :return: dict
    """
    parser = argparse.ArgumentParser()

    # 定义参数
    parser.add_argument("-v", "--version", action='version', version=get_version(), help="show version")

    parser.add_argument("generator", help="模板生成器名称")
    parser.add_argument("name", help="生成的文件名称")

    # 接收不定参数 ref: https://www.it1352.com/1940397.html
    parsed, unknown = parser.parse_known_args()

    for arg in unknown:
        if arg.startswith(("-", "--")):
            parser.add_argument(arg)

    # 解析
    args = parser.parse_args()

    return dict(args._get_kwargs())
