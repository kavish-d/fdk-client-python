"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class LocationIntegrationType(Schema):

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    

