"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class InventoryExportJob(BaseSchema):
    # Catalog swagger.json

    
    seller_id = fields.Int(required=False)
    
    trigger_on = fields.Str(required=False)
    
    request_params = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    completed_on = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    

