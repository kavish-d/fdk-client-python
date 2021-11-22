"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class UpdateDomain(Schema):

    
    _id = fields.Str(required=False)
    

