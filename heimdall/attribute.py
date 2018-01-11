class BaseAttribute(object):
    def __init__(self, required=False):
        self.required = required

    def validate(self, data):
        raise NotImplementedError()


class StringAttribute(BaseAttribute):
    def validate(self, data):
        if not isinstance(data, str):
            raise
        return True


class ArrayAttribute(BaseAttribute):
    def __init__(self, item_attribute, **kwargs):
        self.item_attribute = item_attribute
        super(ArrayAttribute, self).__init__(**kwargs)

    def validate(self, data):
        if not isinstance(data, list):
            raise
        for item in data:
            self.item_attribute.validate(item)
        return True
