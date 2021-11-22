"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class DateMeta(Schema):

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

