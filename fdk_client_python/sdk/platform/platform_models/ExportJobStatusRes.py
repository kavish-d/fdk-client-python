"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ExportJobStatusRes(BaseSchema):

    
    status = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    
    download_url = fields.Str(required=False)
    

