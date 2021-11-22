"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class FileStorageValidator:
    
    class startUpload(Schema):
        
        namespace = fields.Str(required=False)
         
    
    class completeUpload(Schema):
        
        namespace = fields.Str(required=False)
         
    