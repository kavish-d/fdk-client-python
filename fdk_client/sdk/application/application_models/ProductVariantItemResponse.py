"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .Media import Media









from .ActionPage import ActionPage






class ProductVariantItemResponse(BaseSchema):
    # Catalog swagger.json

    
    color = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    is_available = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    color_name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    slug = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

