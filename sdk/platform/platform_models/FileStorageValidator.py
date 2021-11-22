"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class FileStorageValidator:
    
    class startUpload(Schema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class completeUpload(Schema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class appStartUpload(Schema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class appCompleteUpload(Schema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getSignUrls(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class copyFiles(Schema):
        
        sync = fields.Boolean(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class appCopyFiles(Schema):
        
        sync = fields.Boolean(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Int(required=False)
         
    
    class browse(Schema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class browse(Schema):
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class proxy(Schema):
        
        company_id = fields.Int(required=False)
        
        url = fields.Str(required=False)
         
    