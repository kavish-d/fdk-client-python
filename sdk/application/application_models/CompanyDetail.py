"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class CompanyDetail(Schema):

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

