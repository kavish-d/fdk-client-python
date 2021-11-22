"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ItemQuery(Schema):

    
    item_code = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    

