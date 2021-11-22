"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class CommunicationValidator:
    
    class getCommunicationConsent(Schema):
        
        pass 
    
    class upsertCommunicationConsent(Schema):
        
        pass 
    
    class upsertAppPushtoken(Schema):
        
        pass 
    