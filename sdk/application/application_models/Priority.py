"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class Priority(Schema):

    
    key = fields.Str(required=False, validate=OneOf(PriorityEnum.__members__.keys()))
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    

