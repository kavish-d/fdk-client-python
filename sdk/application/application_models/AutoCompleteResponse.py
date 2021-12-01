"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AutocompleteItem import AutocompleteItem


class AutoCompleteResponse(BaseSchema):

    
    items = fields.List(fields.Nested(AutocompleteItem, required=False), required=False)
    

