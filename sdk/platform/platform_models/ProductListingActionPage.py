"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ProductListingActionPage(Schema):

    
    type = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    

