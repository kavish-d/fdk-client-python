"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Links(Schema):

    
    title = fields.Str(required=False)
    
    link = fields.Str(required=False)
    

