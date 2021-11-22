"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class RegisterRequiredFieldsEmail(Schema):

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    

