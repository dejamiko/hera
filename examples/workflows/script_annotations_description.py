from hera.shared._base_model import BaseModel
from hera.workflows import Workflow, script, Parameter
from hera.workflows.models import ValueFrom
from typing import Annotated, Optional, List, Any


class InputParameter(BaseModel):
    default: Optional[Any]
    description: Optional[str]
    enum: Optional[List[Any]]
    value_from: Optional[ValueFrom]

# Old style
#
@script(inputs=[Parameter(name="an_int", description="an_int parameter")])
def echo_int(an_int):
    print(an_int)

@script(inputs=[Parameter(name="a_bool", description="a_bool parameter")])
def echo_boolean(a_bool):
    print(a_bool)

@script(inputs=[Parameter(name="a_string", description="a_string parameter")])
def echo_string(a_string):
    print(a_string)

# New style

# @script()
# def echo_int(an_int: Annotated[int, InputParameter(description="an_int parameter")]):
#     print(an_int)

# @script()
# def echo_boolean(a_bool: Annotated[bool, InputParameter(description="a_bool parameter")]):
#     print(a_bool)

# @script()
# def echo_string(a_string: Annotated[str, InputParameter(description="a_string parameter")]):
#     print(a_string)

with Workflow(generate_name="test-types-", entrypoint="echo") as w:
    echo_int(an_int=1)
    echo_boolean(a_bool=True)
    echo_string(a_string="a")
