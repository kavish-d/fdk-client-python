"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Media import Media







from .ProductListingAction import ProductListingAction

from .ImageUrls import ImageUrls






class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    

