"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .BasePrice import BasePrice

from .BasePrice import BasePrice


class ArticlePriceInfo(Schema):

    
    base = fields.Nested(BasePrice, required=False)
    
    converted = fields.Nested(BasePrice, required=False)
    

