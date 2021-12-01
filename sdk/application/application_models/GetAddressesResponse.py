"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Address import Address


class GetAddressesResponse(BaseSchema):

    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    

