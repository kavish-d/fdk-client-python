"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class Hierarchy(BaseSchema):

    
    department = fields.Int(required=False)
    
    l1 = fields.Int(required=False)
    
    l2 = fields.Int(required=False)
    

