"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class TriggerJobRequest(Schema):

    
    job_id = fields.Str(required=False)
    

