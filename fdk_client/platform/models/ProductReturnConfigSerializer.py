"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ProductReturnConfigSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    store_uid = fields.Int(required=False)
    
    on_same_store = fields.Boolean(required=False)
    

