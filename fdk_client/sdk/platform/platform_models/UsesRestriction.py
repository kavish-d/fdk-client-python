"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .UsesRemaining import UsesRemaining

from .UsesRemaining import UsesRemaining


class UsesRestriction(BaseSchema):

    
    maximum = fields.Nested(UsesRemaining, required=False)
    
    remaining = fields.Nested(UsesRemaining, required=False)
    
