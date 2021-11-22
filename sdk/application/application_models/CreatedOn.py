"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class CreatedOn(Schema):

    
    user_agent = fields.Str(required=False)
    

