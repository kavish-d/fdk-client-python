"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
















class InventoryExportJob(BaseSchema):

    
    status = fields.Str(required=False)
    
    completed_on = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    request_params = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    trigger_on = fields.Str(required=False)
    

