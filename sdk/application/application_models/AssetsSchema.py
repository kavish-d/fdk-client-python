"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .UmdJs import UmdJs

from .CommonJs import CommonJs

from .Css import Css


class AssetsSchema(Schema):

    
    umd_js = fields.Nested(UmdJs, required=False)
    
    common_js = fields.Nested(CommonJs, required=False)
    
    css = fields.Nested(Css, required=False)
    

