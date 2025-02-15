"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class AggregatorRoute(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    payment_flow = fields.Str(required=False)
    
    api_link = fields.Str(required=False)
    

