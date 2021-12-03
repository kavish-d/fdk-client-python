"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class RegisterRequiredFieldsMobile(BaseSchema):

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    
