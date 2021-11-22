"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class CategoryInfo(Schema):

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

