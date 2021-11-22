"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class FormRegisterRequestSchemaPhone(Schema):

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    

