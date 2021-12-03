"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

class LogisticValidator:
    
    class getTatProduct(BaseSchema):
        
        pass 
    
    class getPincodeCity(BaseSchema):
        
        pincode = fields.Str(required=False)
         
    