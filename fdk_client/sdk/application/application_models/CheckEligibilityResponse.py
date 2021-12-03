"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Access import Access


class CheckEligibilityResponse(BaseSchema):

    
    access = fields.Nested(Access, required=False)
    
