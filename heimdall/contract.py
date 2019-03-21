from heimdall.attribute import BaseAttribute
from heimdall.exceptions import ValidationException


class BaseContract(object):

    @property
    def _attributes(self):
        return self._get_attributes()

    @classmethod
    def _get_attributes(cls):
        attributes = {}
        for attribute, value in cls.__dict__.items():
            if isinstance(value, BaseAttribute):
                attributes[attribute] = value
        return attributes

    def validate(self, data):
        errors = {}
        for key, value in data.items():
            attribute = getattr(self, key)
            try:
                attribute.validate(value)
            except ValidationException as e:
                errors[key] = e.message

        for name, attribute in self._attributes.items():
            if name not in data and attribute.required is True:
                errors[name] = "Data is missing Property '%s'" % name
        
        if errors:
            raise 
