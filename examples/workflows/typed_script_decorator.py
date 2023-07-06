from pathlib import Path
from hera.shared._base_model import BaseModel
from hera.workflows import Artifact, DAG, Container, Parameter, Script, Task, Workflow, WorkflowTemplate, script
from hera.workflows.models import TemplateRef, ValueFrom
from typing import Annotated, Optional, List, Any


# How can we avoid the duplication of "an_int" in the inputs for its enum?
# What about descriptions? Do Artifacts need improvement?
# @script(inputs=[Parameter(name="an_int", enum=[1, 2, 3]), Artifact(name="my-art", from_="/tmp/path")])
# def echo(message: str, a_dict: dict, an_int: int = 1):
#     print(message)
#     print(a_dict)
#     print(an_int)
#     with open("/tmp/path", "r") as f:
#         print(f.readlines())


# Use typing.Annotated!
# "Parameters" are reused in the Argo spec/repo in places where it would be
# better to have separate types for "InputParameter", "InputArgument", "OutputParameter" etc

# e.g. "global_name" for an input parameter doesn't make sense

# For arguments, they will just need a name and value (I don't think value_from is
# applicable for args?)

#   default      -> Not applicable for arguments
#   description  -> Not applicable for arguments
#   enum         -> Not applicable for arguments, or output parameters
#   global_name  -> Not applicable for inputs and arguments?
#   name         -> Required for all
#   value        -> Not generally applicable for parameters?
#   value_from   -> Not applicable for arguments


# class InputParameter(BaseModel):
#     default: Optional[Any]
#     description: Optional[str]
#     enum: Optional[List[Any]]
#     global_name: Optional[str]
#     name: str
#     value_from: Optional[ValueFrom]


# class OutputParameter(BaseModel):
#     default: Optional[Any]
#     description: Optional[str]
#     enum: Optional[List[Any]]
#     global_name: Optional[str]
#     name: str
#     value_from: Optional[ValueFrom]


# class InputArtifact(BaseModel):
#     path: str

#     def read_text(self) -> str:
#         return Path(self.path).read_text()


# # Artifacts could be improved to be args to the function, and add access contents easily?
# @script()
# def an_artifact(my_art: InputArtifact(path="/path")):
#     my_art_text = my_art.read_text()


# # vs current
# @script(inputs=Artifact(name="my_art", path="/path"))
# # name is actually unused!
# def an_artifact():
#     # We have to repeat path string unless defined outside of the function
#     my_art_text = Path("/path").read_text()


# @script(
#     inputs=[Parameter(name="an_int", enum=[1, 2, 3])],
#     outputs=[OutputParameter(name="an-output", value_from="/path")],
# )
# def annotated_echo(
#     message: Annotated[
#         str,
#         InputParameter(description="A message to echo to stdout"),
#     ],
#     a_dict: dict,
#     an_int: Annotated[int, InputParameter(enum=[1, 2, 3])] = 1,
# ):
#     print(message)
#     print(a_dict)
#     print(an_int)

#     with open("/path", "w") as f:
#         f.write("some content for the file!")



# @script(inputs=[Parameter(name="an_int", enum=[1, 2, 3])])
# def echo(an_int: int = 1):
#     print(an_int)

class InputParameter(BaseModel):
    default: Optional[Any]
    description: Optional[str]
    enum: Optional[List[Any]]
    global_name: Optional[str]
    # name: str
    value_from: Optional[ValueFrom]

@script()
def echo(an_int: Annotated[int, InputParameter(enum=[1, 2, 3])], another_int):
    print(an_int)
    print(another_int)

with Workflow(generate_name="test-types-", entrypoint="echo") as w:
    echo(an_int=1, another_int=2)
