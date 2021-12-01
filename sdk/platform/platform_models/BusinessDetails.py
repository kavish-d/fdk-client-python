"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Website import Website


class BusinessDetails(BaseSchema):

    
    website = fields.Nested(Website, required=False)
    

