"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class DepartmentIdentifier(Schema):

    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

