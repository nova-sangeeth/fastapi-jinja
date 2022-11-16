"""
Check if the method declarations are modified.
Check if there are more than three methods present in the class and check their types.
Check if there are additional imports being added

"""

import re
data = {
    "version_id": "7",
    "row_id": "29",
    "created_by": "nova@gitaa.in",
    "created_on": "2022-11-07 20:30:20",
    "last_updated_by": "nova@gitaa.in",
    "updated_on": "2022-11-07 20:48:42",
    "is_soft_deleted": 0,
    "last_step": "Q_PYGEN_CODE",
    "question_class": "DYNAMIC",
    "question_type": "NUMERIC_FIB",
    "question_txt_html": "<p>Testing Ace Editor</p>\n",
    "txt_fib_solution_html": None,
    "numeric_solution": None,
    "question_options": None,
    "form_builder_data": "[{\"type\": \"number\", \"required\": false, \"label\": \"Number\", \"placeholder\": \"Test\", \"className\": \"form-control\", \"name\": \"number-test\", \"value\": \"12\", \"min\": 10, \"max\": 12, \"step\": 12}]",
    "params": "{\"number-test\": {\"type\": \"number\", \"value\": 12.0, \"min\": 10.0, \"max\": 12.0}}",
    "py_code_data": "{\"code\": \"# add your imports here\\nfrom numpy.random import Generator\\n\\n\\nclass QuestionTemplate(AbstractQuestionTemplate):\\n\\n    @classmethod\\n    def validate_params(cls, params: ParametersModel) -> None:\\n        pass\\n\\n    @classmethod\\n    def generate(cls, params: ParametersModel, rng: Generator) -> BaseModel:\\n        pass\\n\\n    @classmethod\\n    def test_cases(cls, params: ParametersModel, question_model: BaseModel) -> None:\\n        pass\\n\", \"nonEditableLines\": [[0, 2], [3, 5], [5, 8], [9, 12], [13, 16]], \"methodLines\": [7, 11, 15]}",
    "question_template_uuid": "a4a7a257fc0340ac93bfe9e93e46a23d",
    "template_bank_id": "3"
}

class_definition = """import random
                    class QuestionTemplate():"""
method_definition = """def validate_params(cls, params: random.choice) -> None:"""
classmethod_decorator_definition = """def test_cases(cls, params: random.choice, question_model: random.seed(a=1)) -> None:"""


python_data = data["py_code_data"]

