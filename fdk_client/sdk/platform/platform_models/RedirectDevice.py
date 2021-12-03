"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class RedirectDevice(BaseSchema):

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

