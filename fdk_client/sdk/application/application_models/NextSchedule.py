"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class NextSchedule(BaseSchema):

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
