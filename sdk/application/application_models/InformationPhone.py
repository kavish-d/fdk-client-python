"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class InformationPhone(Schema):

    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    

