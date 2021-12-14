"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class ReqConfiguration(BaseSchema):
    # FileStorage swagger.json

    
    concurrency = fields.Int(required=False)
    

