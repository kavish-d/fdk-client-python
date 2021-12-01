"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema














class MkpLogsResp(BaseSchema):

    
    start_time_iso = fields.Str(required=False)
    
    end_time_iso = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    count = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

