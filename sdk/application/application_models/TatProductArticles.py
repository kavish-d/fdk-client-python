"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .LogisticResponseCategory import LogisticResponseCategory

from .LogisticPromise import LogisticPromise


class TatProductArticles(Schema):

    
    error = fields.Dict(required=False)
    
    category = fields.Nested(LogisticResponseCategory, required=False)
    
    promise = fields.Nested(LogisticPromise, required=False)
    

