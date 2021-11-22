"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .AutocompleteItem import AutocompleteItem


class AutoCompleteResponse(Schema):

    
    items = fields.List(fields.Nested(AutocompleteItem, required=False), required=False)
    

