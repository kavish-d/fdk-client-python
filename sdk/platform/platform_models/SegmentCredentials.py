"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class SegmentCredentials(Schema):

    
    write_key = fields.Str(required=False)
    

