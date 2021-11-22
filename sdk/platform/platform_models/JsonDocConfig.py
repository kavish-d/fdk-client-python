"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .PropBeanConfig import PropBeanConfig


class JsonDocConfig(Schema):

    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    

