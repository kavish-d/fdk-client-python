"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Website import Website


class BusinessDetails(Schema):

    
    website = fields.Nested(Website, required=False)
    

