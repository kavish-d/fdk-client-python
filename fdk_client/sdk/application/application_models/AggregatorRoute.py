"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class AggregatorRoute(BaseSchema):

    
    data = fields.Dict(required=False)
    
    payment_flow = fields.Str(required=False)
    
    api_link = fields.Str(required=False)
    

