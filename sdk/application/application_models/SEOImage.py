"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class SEOImage(Schema):

    
    url = fields.Str(required=False)
    

