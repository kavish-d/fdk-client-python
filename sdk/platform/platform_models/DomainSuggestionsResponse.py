"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .DomainSuggestion import DomainSuggestion


class DomainSuggestionsResponse(Schema):

    
    domains = fields.List(fields.Nested(DomainSuggestion, required=False), required=False)
    

