"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class ThemeValidator:
    
    class getAllPages(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class createPage(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class updateMultiplePages(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class getPage(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
    
    class updatePage(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
    
    class deletePage(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
        
        page_value = fields.Str(required=False)
         
    
    class getThemeLibrary(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class addToThemeLibrary(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class applyTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class isUpgradable(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class upgradeTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class getPublicThemes(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
    
    class createTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppliedTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getFonts(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getThemeById(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class updateTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class deleteTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class getThemeForPreview(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class publishTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class unpublishTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class archiveTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    
    class unarchiveTheme(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        theme_id = fields.Str(required=False)
         
    