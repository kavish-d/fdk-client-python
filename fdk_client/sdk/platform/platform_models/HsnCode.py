"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .HsnCodesObject import HsnCodesObject


class HsnCode(BaseSchema):

    
    data = fields.Nested(HsnCodesObject, required=False)
    
