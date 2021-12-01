"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ProductBulkAssets(BaseSchema):

    
    url = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    user = fields.Dict(required=False)
    

