"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .HistoryPretty import HistoryPretty

from .Page import Page




class HistoryRes(BaseSchema):

    
    items = fields.List(fields.Nested(HistoryPretty, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    points = fields.Float(required=False)
    

