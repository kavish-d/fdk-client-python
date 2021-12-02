"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .GlobalSchemaProps import GlobalSchemaProps


class GlobalSchema(BaseSchema):

    
    props = fields.List(fields.Nested(GlobalSchemaProps, required=False), required=False)
    

