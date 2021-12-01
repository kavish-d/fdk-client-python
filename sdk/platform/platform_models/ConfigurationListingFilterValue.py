"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema









from .ConfigurationBucketPoints import ConfigurationBucketPoints


class ConfigurationListingFilterValue(BaseSchema):

    
    value = fields.Str(required=False)
    
    condition = fields.Str(required=False)
    
    map = fields.Dict(required=False)
    
    sort = fields.Str(required=False)
    
    bucket_points = fields.List(fields.Nested(ConfigurationBucketPoints, required=False), required=False)
    

