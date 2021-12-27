"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ConfigurationBucketPoints(BaseSchema):
    # Catalog swagger.json

    
    end = fields.Float(required=False)
    
    start = fields.Float(required=False)
    

