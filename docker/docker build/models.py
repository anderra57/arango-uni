from arango_orm import Collection
from arango_orm.fields import String
from marshmallow.fields import Email


class Students(Collection):
    __collection__ = "students"
    _key = String(required=True)
    id_number = String(required=True)
    first_name = String(required=True)
    last_name = String(required=True)
    gender = String(required=True)
    email = String(required=True)
    phone = String(required=True)
    mark_tia = String()
    mark_sist = String()
    mark_mining = String()

    def __str__(self):
        return "<Subject({})>".format(self.id_number)
