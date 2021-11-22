"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ProductBulkAssets(Schema):

    
    user = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

