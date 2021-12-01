"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema





from .Media import Media







from .ActionPage import ActionPage






class ProductVariantItemResponse(BaseSchema):

    
    value = fields.Str(required=False)
    
    color_name = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    color = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

