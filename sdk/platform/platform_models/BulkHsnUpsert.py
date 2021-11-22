"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .HsnUpsert import HsnUpsert


class BulkHsnUpsert(Schema):

    
    data = fields.List(fields.Nested(HsnUpsert, required=False), required=False)
    

