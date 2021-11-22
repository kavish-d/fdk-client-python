"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class AvailablePageSectionMetaAttributes(Schema):

    
    attributes = fields.Dict(required=False)
    

