"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class FeedbackValidator:
    
    class createAbuseReport(Schema):
        
        pass 
    
    class updateAbuseReport(Schema):
        
        pass 
    
    class getAbuseReports(Schema):
        
        entity_id = fields.Str(required=False)
        
        entity_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getAttributes(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createAttribute(Schema):
        
        pass 
    
    class getAttribute(Schema):
        
        slug = fields.Str(required=False)
         
    
    class updateAttribute(Schema):
        
        slug = fields.Str(required=False)
         
    
    class createComment(Schema):
        
        pass 
    
    class updateComment(Schema):
        
        pass 
    
    class getComments(Schema):
        
        entity_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class checkEligibility(Schema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
         
    
    class deleteMedia(Schema):
        
        ids = fields.List(fields.Str(required=False), required=False)
         
    
    class createMedia(Schema):
        
        pass 
    
    class updateMedia(Schema):
        
        pass 
    
    class getMedias(Schema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getReviewSummaries(Schema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createReview(Schema):
        
        pass 
    
    class updateReview(Schema):
        
        pass 
    
    class getReviews(Schema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        media = fields.Str(required=False)
        
        rating = fields.List(fields.Float(required=False), required=False)
        
        attribute_rating = fields.List(fields.Str(required=False), required=False)
        
        facets = fields.Boolean(required=False)
        
        sort = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        approve = fields.Boolean(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getTemplates(Schema):
        
        template_id = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        entity_type = fields.Str(required=False)
         
    
    class createQuestion(Schema):
        
        pass 
    
    class updateQuestion(Schema):
        
        pass 
    
    class getQuestionAndAnswers(Schema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        show_answer = fields.Boolean(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getVotes(Schema):
        
        id = fields.Str(required=False)
        
        ref_type = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createVote(Schema):
        
        pass 
    
    class updateVote(Schema):
        
        pass 
    