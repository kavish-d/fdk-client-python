"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class RewardsArticle(Schema):

    
    id = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    price = fields.Float(required=False)
    

