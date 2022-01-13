"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class AggregatorRoute(BaseSchema):
    # Payment swagger.json

    
    payment_flow = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    api_link = fields.Str(required=False)
    

