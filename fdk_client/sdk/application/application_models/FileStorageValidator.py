"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

class FileStorageValidator:
    
    class startUpload(BaseSchema):
        
        namespace = fields.Str(required=False)
         
    
    class completeUpload(BaseSchema):
        
        namespace = fields.Str(required=False)
         
    
    class signUrls(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    