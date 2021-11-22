"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .AttributeObject import AttributeObject




class ReviewRating(Schema):

    
    attributes = fields.List(fields.Nested(AttributeObject, required=False), required=False)
    
    value = fields.Float(required=False)
    

