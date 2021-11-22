"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class DefaultCurrency(Schema):

    
    ref = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

