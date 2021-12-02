"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .AppFeature import AppFeature


class AppFeatureResponse(BaseSchema):

    
    feature = fields.Nested(AppFeature, required=False)
    

