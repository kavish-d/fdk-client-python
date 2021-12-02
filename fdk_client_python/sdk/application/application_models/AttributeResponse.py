"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Attribute import Attribute

from .Page import Page


class AttributeResponse(BaseSchema):

    
    items = fields.List(fields.Nested(Attribute, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

