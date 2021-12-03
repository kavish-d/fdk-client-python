"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class InformationSupport(BaseSchema):

    
    phone = fields.List(fields.Str(required=False), required=False)
    
    email = fields.List(fields.Str(required=False), required=False)
    
    timing = fields.Str(required=False)
    
