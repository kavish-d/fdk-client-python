"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Ownership(BaseSchema):

    
    payable_by = fields.Str(required=False)
    
    payable_category = fields.Str(required=False)
    

