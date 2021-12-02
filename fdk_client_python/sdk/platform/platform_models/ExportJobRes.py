"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ExportJobRes(BaseSchema):

    
    status = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    

