"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class InsertResponse(Schema):

    
    ids = fields.Str(required=False)
    

