"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class DomainStatus(Schema):

    
    display = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    

