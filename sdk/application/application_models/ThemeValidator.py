"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class ThemeValidator:
    
    class getAllPages(Schema):
        
        theme_id = fields.Str(required=False)
         
    
    class getPage(Schema):
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
    
    class getAppliedTheme(Schema):
        
        pass 
    
    class getThemeForPreview(Schema):
        
        theme_id = fields.Str(required=False)
         
    