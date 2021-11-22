"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .HistoryPretty import HistoryPretty

from .Page import Page




class HistoryRes(Schema):

    
    items = fields.List(fields.Nested(HistoryPretty, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    points = fields.Float(required=False)
    

