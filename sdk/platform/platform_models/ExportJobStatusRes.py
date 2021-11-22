"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ExportJobStatusRes(Schema):

    
    status = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    
    download_url = fields.Str(required=False)
    

