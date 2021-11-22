"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class GetLogsListReq(Schema):

    
    marketplace_name = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    

