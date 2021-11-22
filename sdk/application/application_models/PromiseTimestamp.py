"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class PromiseTimestamp(Schema):

    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    

