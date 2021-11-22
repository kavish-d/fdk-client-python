"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .LogisticRequestCategory import LogisticRequestCategory


class TatReqProductArticles(Schema):

    
    category = fields.Nested(LogisticRequestCategory, required=False)
    

