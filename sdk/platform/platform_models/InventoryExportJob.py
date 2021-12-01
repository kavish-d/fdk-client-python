"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
















class InventoryExportJob(BaseSchema):

    
    trigger_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    completed_on = fields.Str(required=False)
    
    request_params = fields.Dict(required=False)
    

