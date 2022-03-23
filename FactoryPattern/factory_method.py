# coding:utf-8

import json
import xml.etree.ElementTree as etree


class JsonConn:
    def __init__(self, path):
        self.data = dict()
        with open(path, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConn:
    def __init__(self, path):
        self.tree = etree.parse(path)

    @property
    def parsed_data(self):
        return self.tree


def conn_factory(path):
    if path.endwith("json"):
        connector = JsonConn
    elif path.endwith("xml"):
        connector = XMLConn
    else:
        raise ValueError(f"cannot connect to {path}")
    return connector(path)


def conn(path):
    factory = None
    try:
        factory = conn_factory(path)
    except ValueError as e:
        print(e)
    return factory


def main():
    f = conn("/data/xxx.json")
    if not f:
        pass
    data = f.parsed_data
    # do sth with data
