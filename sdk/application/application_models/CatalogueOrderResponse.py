"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .RewardsArticle import RewardsArticle


class CatalogueOrderResponse(Schema):

    
    articles = fields.List(fields.Nested(RewardsArticle, required=False), required=False)
    

