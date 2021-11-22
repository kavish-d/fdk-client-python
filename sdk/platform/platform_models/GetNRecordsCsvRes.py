"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .GetNRecordsCsvResItems import GetNRecordsCsvResItems


class GetNRecordsCsvRes(Schema):

    
    items = fields.List(fields.Nested(GetNRecordsCsvResItems, required=False), required=False)
    

