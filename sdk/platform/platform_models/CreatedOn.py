"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class CreatedOn(Schema):

    
    user_agent = fields.Str(required=False)
    

