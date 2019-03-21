from heimdall import BaseContract, StringAttribute, ArrayAttribute, ObjectAttribute


class UserContract(BaseContract):
    name = StringAttribute(required=True)
    hobbies = ArrayAttribute(StringAttribute, required=True)
    # student = ObjectAttribute(StudentContract)

class StudentContract(UserContract):
    grade = StringAttribute(required=True)


data = {"name": "Guido", "hobbies": ["programming", "reading"], "grade": "7"}

contract = StudentContract()
contract.validate(data)

