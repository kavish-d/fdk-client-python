"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class HsnCodesObject(BaseSchema):
    # Catalog swagger.json

    
    hsn_code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    tax1 = fields.Float(required=False)
    
    threshold1 = fields.Float(required=False)
    
    tax2 = fields.Float(required=False)
    
    tax_on_mrp = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    threshold2 = fields.Float(required=False)
    
    tax_on_esp = fields.Boolean(required=False)
    
    hs2_code = fields.Str(required=False)
    

