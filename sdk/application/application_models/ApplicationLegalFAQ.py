"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ApplicationLegalFAQ(BaseSchema):

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    

