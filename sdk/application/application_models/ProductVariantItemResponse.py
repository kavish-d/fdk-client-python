"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *









from .Media import Media



from .ActionPage import ActionPage






class ProductVariantItemResponse(Schema):

    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    color_name = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    color = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

