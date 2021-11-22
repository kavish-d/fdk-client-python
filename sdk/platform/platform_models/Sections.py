"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class Sections(Schema):

    
    attributes = fields.Str(required=False)
    

