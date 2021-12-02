"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class LogisticTimestamp(BaseSchema):

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    

