"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class TeaserTag(Schema):

    
    url = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    

