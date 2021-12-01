"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class IfscCodeResponse(BaseSchema):

    
    bank_name = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

