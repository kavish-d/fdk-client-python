"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .AppStaff import AppStaff


class AppStaffResponse(Schema):

    
    staff_users = fields.List(fields.Nested(AppStaff, required=False), required=False)
    

