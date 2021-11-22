"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class AggregatorRoute(Schema):

    
    api_link = fields.Str(required=False)
    
    payment_flow = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    

