"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class DeviceMeta(BaseSchema):

    
    app_version = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    

