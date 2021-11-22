"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .LandingPageSchema import LandingPageSchema




class LandingPage(Schema):

    
    data = fields.Nested(LandingPageSchema, required=False)
    
    success = fields.Boolean(required=False)
    

