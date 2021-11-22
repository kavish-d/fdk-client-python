"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class ContentValidator:
    
    class getAnnouncements(Schema):
        
        pass 
    
    class getBlog(Schema):
        
        slug = fields.Str(required=False)
        
        root_id = fields.Str(required=False)
         
    
    class getBlogs(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getFaqs(Schema):
        
        pass 
    
    class getFaqCategories(Schema):
        
        pass 
    
    class getFaqBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getFaqCategoryBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getFaqsByCategorySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getLandingPage(Schema):
        
        pass 
    
    class getLegalInformation(Schema):
        
        pass 
    
    class getNavigations(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getPage(Schema):
        
        slug = fields.Str(required=False)
        
        root_id = fields.Str(required=False)
         
    
    class getPages(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getSEOConfiguration(Schema):
        
        pass 
    
    class getSlideshows(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getSlideshow(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getSupportInformation(Schema):
        
        pass 
    
    class getTags(Schema):
        
        pass 
    
    class getPageV2(Schema):
        
        slug = fields.Str(required=False)
        
        root_id = fields.Str(required=False)
         
    
    class getPagesV2(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    