var  python_code = `
# add your imports here
from numpy.random import Generator

class QuestionTemplate(AbstractQuestionTemplate):

    @classmethod
    def validate_params(cls, params: ParametersModel) -> None:
        pass

    @classmethod
    def generate(cls, params: ParametersModel, rng: Generator) -> BaseModel:
        pass

    @classmethod
    def test_cases(cls, params: ParametersModel, question_model: BaseModel) -> None:
        pass
`