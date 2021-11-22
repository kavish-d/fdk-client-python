"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *











from .VerifiedBy import VerifiedBy

from .ProductDownloadItemsData import ProductDownloadItemsData








class ProductDownloadsItems(Schema):

    
    completed_on = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    seller_id = fields.Float(required=False)
    
    template_tags = fields.Dict(required=False)
    
    created_by = fields.Nested(VerifiedBy, required=False)
    
    data = fields.Nested(ProductDownloadItemsData, required=False)
    
    status = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    trigger_on = fields.Str(required=False)
    

