"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Currency import Currency


class CurrenciesResponse(Schema):

    
    items = fields.List(fields.Nested(Currency, required=False), required=False)
    

