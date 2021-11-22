"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class LeadValidator:
    
    class getTickets(Schema):
        
        company_id = fields.Str(required=False)
        
        items = fields.Boolean(required=False)
        
        filters = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        priority = fields.Str(required=False, validate=OneOf(PriorityEnum.__members__.keys()))
        
        category = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createTicket(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getTickets(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        items = fields.Boolean(required=False)
        
        filters = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        priority = fields.Str(required=False, validate=OneOf(PriorityEnum.__members__.keys()))
        
        category = fields.Str(required=False)
         
    
    class getTicket(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class editTicket(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getTicket(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class editTicket(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createHistory(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getTicketHistory(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getFeedbacks(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class submitFeedback(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createHistory(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getTicketHistory(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getCustomForm(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class editCustomForm(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class getCustomForms(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createCustomForm(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getTokenForVideoRoom(Schema):
        
        company_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    
    class getTokenForVideoRoom(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    
    class getVideoParticipants(Schema):
        
        company_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    
    class getVideoParticipants(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    
    class openVideoRoom(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class closeVideoRoom(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        unique_name = fields.Str(required=False)
         
    