"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *







from .JobConfig import JobConfig


class JobConfigRawDTO(Schema):

    
    integration = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    data = fields.Nested(JobConfig, required=False)
    

