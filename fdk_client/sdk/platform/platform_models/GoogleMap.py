"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GoogleMapCredentials import GoogleMapCredentials


class GoogleMap(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(GoogleMapCredentials, required=False)
    

