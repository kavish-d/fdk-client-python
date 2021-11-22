"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class PromiseTimestamp(Schema):

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    

