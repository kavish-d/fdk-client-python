"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Files(Schema):

    
    values = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    

