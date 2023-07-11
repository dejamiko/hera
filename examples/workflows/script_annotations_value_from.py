from hera.shared._base_model import BaseModel
from hera.workflows import Workflow, script, Parameter
from hera.workflows.models import ValueFrom, ConfigMapKeySelector
from typing import Annotated, Optional, List, Any


class InputParameter(BaseModel):
    default: Optional[Any]
    description: Optional[str]
    enum: Optional[List[Any]]
    value_from: Optional[ValueFrom]

# Old style

@script(inputs=[Parameter(name="an_int", value_from=ValueFrom( config_map_key_ref=ConfigMapKeySelector(
                    name="simple-parameters",
                    key="an_int_param"
                )))])
def echo_int():
    print("inputs.parameters.an_int")

@script(inputs=[Parameter(name="a_bool", value_from=ValueFrom( config_map_key_ref=ConfigMapKeySelector(
                    name="simple-parameters",
                    key="a_bool_param"
                )))])
def echo_boolean(a_bool):
    print(a_bool)

@script(inputs=[Parameter(name="a_string", value_from=ValueFrom( config_map_key_ref=ConfigMapKeySelector(
                    name="simple-parameters",
                    key="a_string_param"
                )))])
def echo_string(a_string):
    print(a_string)

# New style

# @script()
# def echo_int(an_int: Annotated[int, InputParameter(value_from=ValueFrom(config_map_key_ref=ConfigMapKeySelector(
#                     name="simple-parameters",
#                     key="an_int_param"
#                 )))]):
#     print(an_int)

# @script()
# def echo_boolean(a_bool: Annotated[bool, InputParameter(value_from=ValueFrom(config_map_key_ref=ConfigMapKeySelector(
#                     name="simple-parameters",
#                     key="a_bool_param"
#                 )))]):
#     print(a_bool)

# @script()
# def echo_string(a_string: Annotated[str, InputParameter(value_from=ValueFrom(config_map_key_ref=ConfigMapKeySelector(
#                     name="simple-parameters",
#                     key="a_string_param"
#                 )))]):
#     print(a_string)

with Workflow(generate_name="test-types-", entrypoint="echo") as w:
    echo_int()
    echo_boolean()
    echo_string()
