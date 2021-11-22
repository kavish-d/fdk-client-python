"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class LogisticValidator:
    
    class getTatProduct(Schema):
        
        pass 
    
    class getPincodeCity(Schema):
        
        pincode = fields.Str(required=False)
         
    