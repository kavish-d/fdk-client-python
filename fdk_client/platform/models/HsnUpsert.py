"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class HsnUpsert(BaseSchema):
    # Catalog swagger.json

    
    tax_on_esp = fields.Boolean(required=False)
    
    tax_on_mrp = fields.Boolean(required=False)
    
    tax1 = fields.Float(required=False)
    
    company_id = fields.Int(required=False)
    
    threshold2 = fields.Float(required=False)
    
    uid = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    tax2 = fields.Float(required=False)
    
    threshold1 = fields.Float(required=False)
    
    hs2_code = fields.Str(required=False)
    

