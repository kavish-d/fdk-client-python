"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class Document(BaseSchema):
    # CompanyProfile swagger.json

    
    type = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    url = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

