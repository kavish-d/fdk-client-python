"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Meta import Meta


class Guide(Schema):

    
    meta = fields.Nested(Meta, required=False)
    

