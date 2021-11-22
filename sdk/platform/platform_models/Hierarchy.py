"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class Hierarchy(Schema):

    
    l1 = fields.Int(required=False)
    
    l2 = fields.Int(required=False)
    
    department = fields.Int(required=False)
    

