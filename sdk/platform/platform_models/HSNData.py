"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class HSNData(Schema):

    
    hsn_code = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.List(fields.Str(required=False), required=False)
    

