"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ApplicationWebsite(Schema):

    
    enabled = fields.Boolean(required=False)
    
    basepath = fields.Str(required=False)
    

