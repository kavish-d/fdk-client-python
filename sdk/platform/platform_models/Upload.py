"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Upload(BaseSchema):

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    

