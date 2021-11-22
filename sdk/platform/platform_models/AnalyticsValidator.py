"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class AnalyticsValidator:
    
    class getStatiscticsGroups(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getStatiscticsGroupComponents(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        group_name = fields.Str(required=False)
         
    
    class getComponentStatsCSV(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        component_name = fields.Str(required=False)
         
    
    class getComponentStatsPDF(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        component_name = fields.Str(required=False)
         
    
    class getComponentStats(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        component_name = fields.Str(required=False)
         
    
    class getAbandonCartList(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getAbandonCartsCSV(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
         
    
    class getAbandonCartDetail(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
         
    
    class createExportJob(Schema):
        
        company_id = fields.Str(required=False)
        
        export_type = fields.Str(required=False)
         
    
    class getExportJobStatus(Schema):
        
        company_id = fields.Str(required=False)
        
        export_type = fields.Str(required=False)
        
        job_id = fields.Str(required=False)
         
    
    class getLogsList(Schema):
        
        company_id = fields.Str(required=False)
        
        log_type = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class searchLogs(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        log_type = fields.Str(required=False)
         
    