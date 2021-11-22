"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .ActionPage import ActionPage



from .Media import Media


class ProductBrand(Schema):

    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    

