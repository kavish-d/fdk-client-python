"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class CDN(Schema):

    
    url = fields.Str(required=False)
    

