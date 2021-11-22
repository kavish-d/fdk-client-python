"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Charges(Schema):

    
    threshold = fields.Float(required=False)
    
    charges = fields.Float(required=False)
    

