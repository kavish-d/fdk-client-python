"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .DomainAdd import DomainAdd


class DomainAddRequest(Schema):

    
    domain = fields.Nested(DomainAdd, required=False)
    

