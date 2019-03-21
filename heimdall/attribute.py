class BaseAttribute(object):
    def __init__(self, required=False):
        self.required = required

    def validate(self, data):
        raise NotImplementedError()


class StringAttribute(BaseAttribute):
    def validate(self, data):
        if not isinstance(data, str):
            raise Exception("Item is not a string")
        return True


class ArrayAttribute(BaseAttribute):
    def __init__(self, item_contract, **kwargs):
        self.item_contract = item_contract()
        super(ArrayAttribute, self).__init__(**kwargs)

    def validate(self, data):
        if not isinstance(data, list):
            raise Exception("Item is not a list")
        for item in data:
            self.item_contract.validate(item)
        return True


class ObjectAttribute(BaseAttribute):
    def __init__(self, contract, **kwargs):
        self.contract = contract()
        super(ObjectAttribute, self).__init__(**kwargs)

    def validate(self, data):
        self.contract.validate(data)
        return True


class IntAttribute(BaseAttribute):
    def validate(self, data):
        if not isinstance(data, int):
            raise Exception("Item is not a integer")
        return True


class BoolAttribute(BaseAttribute):
    def validate(self, data):
        if not isinstance(data, bool):
            raise Exception("Item is not a boolean")
        return True
