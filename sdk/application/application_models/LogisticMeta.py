"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class LogisticMeta(Schema):

    
    zone = fields.Str(required=False)
    
    deliverables = fields.List(fields.Raw(required=False), required=False)
    

