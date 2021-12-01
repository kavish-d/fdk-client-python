"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class HSNData(BaseSchema):

    
    country_of_origin = fields.List(fields.Str(required=False), required=False)
    
    hsn_code = fields.List(fields.Str(required=False), required=False)
    

