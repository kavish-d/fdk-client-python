"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .ProductCompareResponse import ProductCompareResponse


class ProductFrequentlyComparedSimilarResponse(Schema):

    
    similars = fields.Nested(ProductCompareResponse, required=False)
    

