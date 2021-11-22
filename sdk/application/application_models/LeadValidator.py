"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class LeadValidator:
    
    class getTicket(Schema):
        
        id = fields.Str(required=False)
         
    
    class createHistory(Schema):
        
        id = fields.Str(required=False)
         
    
    class createTicket(Schema):
        
        pass 
    
    class getCustomForm(Schema):
        
        slug = fields.Str(required=False)
         
    
    class submitCustomForm(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getParticipantsInsideVideoRoom(Schema):
        
        unique_name = fields.Str(required=False)
         
    
    class getTokenForVideoRoom(Schema):
        
        unique_name = fields.Str(required=False)
         
    