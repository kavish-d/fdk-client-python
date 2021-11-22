"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .UsesRemaining import UsesRemaining

from .UsesRemaining import UsesRemaining


class UsesRestriction(Schema):

    
    remaining = fields.Nested(UsesRemaining, required=False)
    
    maximum = fields.Nested(UsesRemaining, required=False)
    

