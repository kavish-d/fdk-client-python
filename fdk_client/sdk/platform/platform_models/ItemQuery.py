"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ItemQuery(BaseSchema):
    # Catalog swagger.json

    
    item_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    brand_uid = fields.Int(required=False)
    

