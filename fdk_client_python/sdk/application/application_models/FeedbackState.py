"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema














class FeedbackState(BaseSchema):

    
    active = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    media = fields.Str(required=False)
    
    qna = fields.Boolean(required=False)
    
    rating = fields.Boolean(required=False)
    
    review = fields.Boolean(required=False)
    

