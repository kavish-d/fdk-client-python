"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Upload(Schema):

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    

