"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Access import Access


class CheckEligibilityResponse(Schema):

    
    access = fields.Nested(Access, required=False)
    

