"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .SizeChartValues import SizeChartValues



from .ColumnHeaders import ColumnHeaders








class SizeChart(Schema):

    
    size_tip = fields.Str(required=False)
    
    sizes = fields.List(fields.Nested(SizeChartValues, required=False), required=False)
    
    image = fields.Str(required=False)
    
    headers = fields.Nested(ColumnHeaders, required=False)
    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    

