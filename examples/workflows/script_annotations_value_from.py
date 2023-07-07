from hera.shared._base_model import BaseModel
from hera.workflows import Workflow, script, Parameter
from hera.workflows.models import ValueFrom
from typing import Annotated, Optional, List, Any


class InputParameter(BaseModel):
    default: Optional[Any]
    description: Optional[str]
    enum: Optional[List[Any]]
    global_name: Optional[str]
    value_from: Optional[ValueFrom]

# Old style
#
# @script(inputs=[Parameter(name="an_int", value_from={"from_an_int": "from_an_int_value"})])
# def echo_int(an_int):
#     print(an_int)

# @script(inputs=[Parameter(name="a_bool", value_from={"from_a_bool_int": "from_a_bool_value"})])
# def echo_boolean(a_bool):
#     print(a_bool)

# @script(inputs=[Parameter(name="a_string", value_from={"from_a_string_int": "from_a_string_value"})])
# def echo_string(a_string):
#     print(a_string)

# New style

@script()
def echo_int(an_int: Annotated[int, InputParameter(value_from={"from_an_int": "from_an_int_value"})]):
    print(an_int)

@script()
def echo_boolean(a_bool: Annotated[bool, InputParameter(value_from={"from_a_bool_int": "from_a_bool_value"})]):
    print(a_bool)

@script()
def echo_string(a_string: Annotated[str, InputParameter(value_from={"from_a_string_int": "from_a_string_value"})]):
    print(a_string)

with Workflow(generate_name="test-types-", entrypoint="echo") as w:
    echo_int(an_int=1)
    echo_boolean(a_bool=True)
    echo_string(a_string="a")
