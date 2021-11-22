"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class DepartmentIdentifier(Schema):

    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    

