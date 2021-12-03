"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .DomainAdd import DomainAdd


class DomainAddRequest(BaseSchema):

    
    domain = fields.Nested(DomainAdd, required=False)
    

