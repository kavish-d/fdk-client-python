"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class LogisticTimestamp(Schema):

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    

