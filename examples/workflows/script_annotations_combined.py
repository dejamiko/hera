from hera.shared._base_model import BaseModel
from hera.workflows import Workflow, script, Parameter
from hera.workflows.models import ValueFrom
from typing import Annotated, Optional, List, Any

from hera.workflows.steps import Steps


class InputParameter(BaseModel):
    default: Optional[Any]
    description: Optional[str]
    enum: Optional[List[Any]]
    value_from: Optional[ValueFrom]

# Old style
# @script(
#     inputs=[
#         Parameter(name="an_int", description="an_int parameter", default=1, enum=[1, 2, 3]), 
#         Parameter(name="a_bool", description="a_bool parameter", default=True, enum=[True, False]), 
#         Parameter(name="a_string", description="a_string parameter", default="a", enum=["a", "b", "c"])
#     ]
# )
# def echo_all(an_int, a_bool, a_string):
#     print(an_int)
#     print(a_bool)
#     print(a_string)


# New style
@script()
def echo_all(
    an_int: Annotated[int, InputParameter(description="an_int parameter", default=1, enum=[1, 2, 3])], 
    a_bool: Annotated[bool, InputParameter(description="a_bool parameter", default=True, enum=[True, False])], 
    a_string: Annotated[str, InputParameter(description="a_string parameter", default="a", enum=["a", "b", "c"])]
):
    print(an_int)
    print(a_bool)
    print(a_string)


with Workflow(generate_name="test-types-", entrypoint="my_steps") as w:
    with Steps(name="my_steps") as s:
        echo_all(an_int=1, a_bool=True, a_string="a")
