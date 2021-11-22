"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class ProductListingActionPage(Schema):

    
    type = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    params = fields.Dict(required=False)
    

