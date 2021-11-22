"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class SupportedLanguage(Schema):

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

