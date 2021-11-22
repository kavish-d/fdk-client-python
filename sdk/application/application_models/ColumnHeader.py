"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class ColumnHeader(Schema):

    
    convertable = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    

