"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class Association(BaseSchema):

    
    company_id = fields.Int(required=False)
    
    application_id = fields.List(fields.Str(required=False), required=False)
    
    extension_id = fields.Str(required=False)
    
    criteria = fields.Str(required=False)
    

