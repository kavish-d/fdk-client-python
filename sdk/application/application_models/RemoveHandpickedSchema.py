"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class RemoveHandpickedSchema(Schema):

    
    tags = fields.List(fields.Str(required=False), required=False)
    

