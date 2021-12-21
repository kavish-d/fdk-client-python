"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .ActionPage import ActionPage

from .Media import Media




class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    

