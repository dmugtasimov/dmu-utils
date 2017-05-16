from __future__ import absolute_import

import json

from schematics import Model


class CustomModel(Model):

    def __init__(self, *args, **kwargs):
        super(CustomModel, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self.to_primitive())

    @classmethod
    def from_json(cls, source, **kwargs):
        return cls(json.loads(source), **kwargs)

    def to_json(self, **kwargs):
        return json.dumps(self.to_primitive(**kwargs), ensure_ascii=False)
