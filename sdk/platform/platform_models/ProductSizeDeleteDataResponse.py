"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ProductSizeDeleteDataResponse(Schema):

    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

