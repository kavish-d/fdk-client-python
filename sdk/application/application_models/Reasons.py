"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *














class Reasons(Schema):

    
    reason_text = fields.Str(required=False)
    
    show_text_area = fields.Boolean(required=False)
    
    feedback_type = fields.Str(required=False)
    
    flow = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    
    priority = fields.Int(required=False)
    

