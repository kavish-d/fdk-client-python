"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ConfigurationBucketPoints(Schema):

    
    start = fields.Float(required=False)
    
    end = fields.Float(required=False)
    

