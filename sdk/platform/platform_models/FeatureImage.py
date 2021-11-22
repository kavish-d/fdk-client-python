"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class FeatureImage(Schema):

    
    secure_url = fields.Str(required=False)
    

