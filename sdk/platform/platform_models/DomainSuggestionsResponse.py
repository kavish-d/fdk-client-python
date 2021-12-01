"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .DomainSuggestion import DomainSuggestion


class DomainSuggestionsResponse(BaseSchema):

    
    domains = fields.List(fields.Nested(DomainSuggestion, required=False), required=False)
    

