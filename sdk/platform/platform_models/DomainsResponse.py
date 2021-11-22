"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Domain import Domain


class DomainsResponse(Schema):

    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    

