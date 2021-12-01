"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .RewardsArticle import RewardsArticle


class CatalogueOrderResponse(BaseSchema):

    
    articles = fields.List(fields.Nested(RewardsArticle, required=False), required=False)
    

