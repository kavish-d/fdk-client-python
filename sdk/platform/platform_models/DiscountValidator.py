"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class DiscountValidator:
    
    class getDiscounts(Schema):
        
        company_id = fields.Int(required=False)
        
        view = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        archived = fields.Boolean(required=False)
        
        month = fields.Int(required=False)
        
        year = fields.Int(required=False)
        
        type = fields.Str(required=False)
        
        app_ids = fields.List(fields.Str(required=False), required=False)
         
    
    class createDiscount(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getDiscount(Schema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateDiscount(Schema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class validateDiscountFile(Schema):
        
        company_id = fields.Int(required=False)
        
        discount = fields.Str(required=False)
         
    
    class downloadDiscountFile(Schema):
        
        company_id = fields.Int(required=False)
        
        type = fields.Str(required=False)
         
    
    class getValidationJob(Schema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class cancelValidationJob(Schema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class getDownloadJob(Schema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    
    class cancelDownloadJob(Schema):
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
    