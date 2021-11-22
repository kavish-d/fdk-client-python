"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class OrderCommitted(Schema):

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    

