"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class AddThemeRequestSchema(Schema):

    
    theme_id = fields.Str(required=False)
    

