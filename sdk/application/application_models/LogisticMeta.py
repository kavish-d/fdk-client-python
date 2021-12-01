"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class LogisticMeta(BaseSchema):

    
    zone = fields.Str(required=False)
    
    deliverables = fields.List(fields.Raw(required=False), required=False)
    

