"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class TriggerJobRequest(BaseSchema):
    # Communication swagger.json

    
    job_id = fields.Str(required=False)
    

