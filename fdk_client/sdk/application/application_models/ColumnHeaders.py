"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ColumnHeader import ColumnHeader

from .ColumnHeader import ColumnHeader

from .ColumnHeader import ColumnHeader

from .ColumnHeader import ColumnHeader

from .ColumnHeader import ColumnHeader

from .ColumnHeader import ColumnHeader


class ColumnHeaders(BaseSchema):

    
    col_2 = fields.Nested(ColumnHeader, required=False)
    
    col_5 = fields.Nested(ColumnHeader, required=False)
    
    col_3 = fields.Nested(ColumnHeader, required=False)
    
    col_1 = fields.Nested(ColumnHeader, required=False)
    
    col_4 = fields.Nested(ColumnHeader, required=False)
    
    col_6 = fields.Nested(ColumnHeader, required=False)
    

