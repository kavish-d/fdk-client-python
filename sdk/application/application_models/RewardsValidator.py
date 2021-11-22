"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class RewardsValidator:
    
    class getPointsOnProduct(Schema):
        
        pass 
    
    class getOfferByName(Schema):
        
        name = fields.Str(required=False)
         
    
    class getOrderDiscount(Schema):
        
        pass 
    
    class getUserPoints(Schema):
        
        pass 
    
    class getUserPointsHistory(Schema):
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getUserReferralDetails(Schema):
        
        pass 
    
    class redeemReferralCode(Schema):
        
        pass 
    