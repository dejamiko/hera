import importlib
from pathlib import Path
import pytest

import yaml
from hera.shared import global_config
from tests.test_examples import _compare_workflows, _generate_yaml
import examples.workflows as hera_examples
from hera.workflows import (
    CronWorkflow as HeraCronWorkflow,
    Workflow as HeraWorkflow,
    WorkflowTemplate as HeraWorkflowTemplate,
)


@pytest.mark.parametrize(
    "name", ["value_from", "default", "description", "enum"]
)
def test_hera_output(name):
    # GIVEN
    module_name = "script_annotations_" + name
    global_config.reset()
    global_config.host = "http://hera.testing"
    workflow = importlib.import_module(f"examples.workflows.{module_name}").w
    generated_yaml_path = Path(hera_examples.__file__).parent / f"{module_name.replace('_', '-')}.yaml"

    # WHEN
    output = workflow.to_dict()

    # THEN
    if _generate_yaml(generated_yaml_path):
        generated_yaml_path.write_text(yaml.dump(output, sort_keys=False, default_flow_style=False))

    # Check there have been no regressions from the generated yaml committed in the repo
    assert generated_yaml_path.exists()
    _compare_workflows(workflow, output, yaml.safe_load(generated_yaml_path.read_text()))

    if isinstance(workflow, HeraWorkflowTemplate):
        assert workflow == HeraWorkflowTemplate.from_dict(workflow.to_dict())
        assert workflow == HeraWorkflowTemplate.from_yaml(workflow.to_yaml())
    elif isinstance(workflow, HeraCronWorkflow):
        assert workflow == HeraCronWorkflow.from_dict(workflow.to_dict())
        assert workflow == HeraCronWorkflow.from_yaml(workflow.to_yaml())
    elif isinstance(workflow, HeraWorkflow):
        assert workflow == HeraWorkflow.from_dict(workflow.to_dict())
        assert workflow == HeraWorkflow.from_yaml(workflow.to_yaml())
