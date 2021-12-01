"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class LocationIntegrationType(BaseSchema):

    
    order = fields.Str(required=False)
    
    inventory = fields.Str(required=False)
    

