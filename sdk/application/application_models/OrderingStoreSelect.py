"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class OrderingStoreSelect(Schema):

    
    uid = fields.Int(required=False)
    

