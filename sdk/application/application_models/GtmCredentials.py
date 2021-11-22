"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class GtmCredentials(Schema):

    
    api_key = fields.Str(required=False)
    

