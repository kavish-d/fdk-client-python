"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Stage import Stage

from .Stages import Stages


class Filters(Schema):

    
    stage = fields.Nested(Stage, required=False)
    
    stages = fields.Nested(Stages, required=False)
    

