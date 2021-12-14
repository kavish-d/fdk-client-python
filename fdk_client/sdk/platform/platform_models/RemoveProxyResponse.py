"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class RemoveProxyResponse(BaseSchema):
    # Partner swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    

