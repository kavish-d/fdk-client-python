"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class SuccessResponse(BaseSchema):

    
    uid = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
