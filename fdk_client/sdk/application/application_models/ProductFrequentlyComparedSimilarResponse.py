"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductCompareResponse import ProductCompareResponse


class ProductFrequentlyComparedSimilarResponse(BaseSchema):

    
    similars = fields.Nested(ProductCompareResponse, required=False)
    

