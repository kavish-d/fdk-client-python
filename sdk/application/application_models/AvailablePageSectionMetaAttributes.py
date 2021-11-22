"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class AvailablePageSectionMetaAttributes(Schema):

    
    attributes = fields.Dict(required=False)
    

