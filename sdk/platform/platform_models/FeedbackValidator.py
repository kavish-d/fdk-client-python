"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class FeedbackValidator:
    
    class getAttributes(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getCustomerReviews(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        entity_type = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        media = fields.Str(required=False)
        
        rating = fields.List(fields.Float(required=False), required=False)
        
        attribute_rating = fields.List(fields.Str(required=False), required=False)
        
        facets = fields.Boolean(required=False)
        
        sort = fields.Str(required=False)
        
        next = fields.Str(required=False)
        
        start = fields.Str(required=False)
        
        limit = fields.Str(required=False)
        
        count = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateApprove(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        review_id = fields.Str(required=False)
         
    
    class getHistory(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        review_id = fields.Str(required=False)
         
    
    class getApplicationTemplates(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createTemplate(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getTemplateById(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateTemplate(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateTemplateStatus(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    