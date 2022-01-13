"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductListingActionPage(BaseSchema):
    # Catalog swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    

