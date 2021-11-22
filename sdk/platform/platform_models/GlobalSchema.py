"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .GlobalSchemaProps import GlobalSchemaProps


class GlobalSchema(Schema):

    
    props = fields.List(fields.Nested(GlobalSchemaProps, required=False), required=False)
    

