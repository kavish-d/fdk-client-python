"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class DpDetails(Schema):

    
    gst_tag = fields.Str(required=False)
    

