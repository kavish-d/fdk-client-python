"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GoogleMapCredentials import GoogleMapCredentials


class GoogleMap(BaseSchema):

    
    credentials = fields.Nested(GoogleMapCredentials, required=False)
    

