"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class OrderFeature(BaseSchema):

    
    buy_again = fields.Boolean(required=False)
    

