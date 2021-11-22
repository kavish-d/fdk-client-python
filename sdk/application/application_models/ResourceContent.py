"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class ResourceContent(Schema):

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

