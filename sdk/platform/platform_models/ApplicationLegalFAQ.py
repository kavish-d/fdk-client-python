"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ApplicationLegalFAQ(Schema):

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    

