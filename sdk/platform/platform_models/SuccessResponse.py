"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class SuccessResponse(Schema):

    
    uid = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    

