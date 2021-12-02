"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class DateMeta(BaseSchema):

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

