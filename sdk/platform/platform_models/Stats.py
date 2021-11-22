"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class Stats(Schema):

    
    _id = fields.Str(required=False)
    
    imported = fields.Raw(required=False)
    
    processed = fields.Raw(required=False)
    

