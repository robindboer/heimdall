# Heimdall
Heimdall will protect your code from bad data structures.

## Example
A short example to show my intent with this package.

```python
from heimdall import BaseContract, StringAttribute, ArrayAttribute


class UserContract(BaseContract):
    name = StringAttribute(required=True)
    hobbies = ArrayAttribute(StringAttribute, required=True)


data = {"name": "Guido", "hobbies": ["programming", "reading"]}

contract = UserContract()
contract.validate(data)

```
