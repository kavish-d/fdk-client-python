"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .AttributeDetail import AttributeDetail


class AttributeMetadata(Schema):

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(AttributeDetail, required=False), required=False)
    

