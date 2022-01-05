"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ConfigurationBucketPoints import ConfigurationBucketPoints


class ConfigurationListingFilterValue(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Str(required=False)
    
    condition = fields.Str(required=False)
    
    map = fields.Dict(required=False)
    
    value = fields.Str(required=False)
    
    bucket_points = fields.List(fields.Nested(ConfigurationBucketPoints, required=False), required=False)
    

