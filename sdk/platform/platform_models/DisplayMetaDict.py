"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class DisplayMetaDict(Schema):

    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

