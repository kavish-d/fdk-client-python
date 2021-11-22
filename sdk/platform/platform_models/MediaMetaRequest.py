"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class MediaMetaRequest(Schema):

    
    max_count = fields.Int(required=False)
    
    size = fields.Int(required=False)
    

