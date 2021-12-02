"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AttributeObject import AttributeObject




class ReviewRating(BaseSchema):

    
    attributes = fields.List(fields.Nested(AttributeObject, required=False), required=False)
    
    value = fields.Float(required=False)
    

