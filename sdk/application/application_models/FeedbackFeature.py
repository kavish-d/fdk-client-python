"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class FeedbackFeature(Schema):

    
    enabled = fields.Boolean(required=False)
    

