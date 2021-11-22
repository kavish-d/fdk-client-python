"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .AppFeature import AppFeature


class AppFeatureRequest(Schema):

    
    feature = fields.Nested(AppFeature, required=False)
    

