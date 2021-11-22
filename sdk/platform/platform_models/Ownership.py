"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Ownership(Schema):

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    

