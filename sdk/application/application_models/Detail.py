"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Detail(Schema):

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

