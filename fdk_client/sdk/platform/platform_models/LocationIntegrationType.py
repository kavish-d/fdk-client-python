"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class LocationIntegrationType(BaseSchema):
    # CompanyProfile swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    

