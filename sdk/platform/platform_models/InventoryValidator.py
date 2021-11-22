"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class InventoryValidator:
    
    class getJobsByCompany(Schema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateJob(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class createJob(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getJobSteps(Schema):
        
        company_id = fields.Int(required=False)
        
        job_id = fields.Int(required=False)
         
    
    class getJobByCompanyAndIntegration(Schema):
        
        company_id = fields.Int(required=False)
        
        integration_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class disable(Schema):
        
        company_id = fields.Int(required=False)
        
        integration_id = fields.Str(required=False)
         
    
    class getJobConfigDefaults(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getJobByCode(Schema):
        
        company_id = fields.Int(required=False)
        
        code = fields.Str(required=False)
         
    
    class getJobCodeMetrics(Schema):
        
        company_id = fields.Int(required=False)
        
        code = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        status = fields.Str(required=False)
        
        date = fields.Str(required=False)
         
    
    class getJobCodesByCompanyAndIntegration(Schema):
        
        company_id = fields.Int(required=False)
        
        integration_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    