"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CouponAuthor(Schema):

    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    

