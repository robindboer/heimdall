from heimdall.attribute import BaseAttribute


class BaseContract(object):
    def __init__(self):
        self._validators = []

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
        for key, value in data.items():
            attribute = getattr(self, key, None)
            if not attribute:
                raise Exception("Value '%s' is Unknown" % key)
            attribute.validate(value)

        for name, attribute in self._attributes.items():
            if name not in data and attribute.required is True:
                raise Exception('Missing Property')
