"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .GenericDTO import GenericDTO


class TaskDTO(Schema):

    
    type = fields.Int(required=False)
    
    group_list = fields.List(fields.Nested(GenericDTO, required=False), required=False)
    

