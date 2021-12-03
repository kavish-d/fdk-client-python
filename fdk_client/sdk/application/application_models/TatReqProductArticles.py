"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .LogisticRequestCategory import LogisticRequestCategory


class TatReqProductArticles(BaseSchema):

    
    category = fields.Nested(LogisticRequestCategory, required=False)
    
