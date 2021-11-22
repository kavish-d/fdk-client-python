"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .SupportedLanguage import SupportedLanguage


class LanguageResponse(Schema):

    
    items = fields.List(fields.Nested(SupportedLanguage, required=False), required=False)
    

