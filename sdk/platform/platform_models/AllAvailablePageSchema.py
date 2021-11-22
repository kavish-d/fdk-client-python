"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .AvailablePageSchema import AvailablePageSchema


class AllAvailablePageSchema(Schema):

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    

