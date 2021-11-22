"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class CDN(Schema):

    
    url = fields.Str(required=False)
    

