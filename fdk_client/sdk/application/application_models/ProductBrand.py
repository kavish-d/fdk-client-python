"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Media import Media

from .ActionPage import ActionPage






class ProductBrand(BaseSchema):

    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
