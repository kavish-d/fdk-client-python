"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class UsesRemaining(BaseSchema):

    
    app = fields.Int(required=False)
    
    user = fields.Int(required=False)
    
    total = fields.Int(required=False)
    

