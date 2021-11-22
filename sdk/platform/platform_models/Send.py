"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Send(Schema):

    
    raw = fields.Boolean(required=False)
    
    processed = fields.Boolean(required=False)
    

