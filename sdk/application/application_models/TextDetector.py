"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class TextDetector(Schema):

    
    confidence = fields.Float(required=False)
    
    text = fields.Str(required=False)
    
    text_class = fields.Str(required=False)
    
    text_type = fields.Str(required=False)
    

