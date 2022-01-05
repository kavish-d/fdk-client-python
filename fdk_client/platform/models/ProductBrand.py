"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Media1 import Media1





from .ProductListingAction import ProductListingAction


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media1, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    

