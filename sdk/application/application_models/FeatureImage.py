"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class FeatureImage(Schema):

    
    secure_url = fields.Str(required=False)
    

