"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class PcrFeature(Schema):

    
    staff_selection = fields.Boolean(required=False)
    

