"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class BagItemAttributes(Schema):

    
    item_code = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    

