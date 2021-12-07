"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class FulfillingStore(BaseSchema):

    
    code = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    company_name = fields.Str(required=False)
    

