"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class ShareValidator:
    
    class getApplicationQRCode(Schema):
        
        pass 
    
    class getProductQRCodeBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getCollectionQRCodeBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getUrlQRCode(Schema):
        
        url = fields.Str(required=False)
         
    
    class createShortLink(Schema):
        
        pass 
    
    class getShortLinkByHash(Schema):
        
        hash = fields.Str(required=False)
         
    
    class getOriginalShortLinkByHash(Schema):
        
        hash = fields.Str(required=False)
         
    