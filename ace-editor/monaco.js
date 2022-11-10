var python_code = `# add your imports here
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
`;

require.config({
  paths: { vs: "https://cdn.jsdelivr.net/npm/monaco-editor@0.34.1/min/vs" },
});
require(["vs/editor/editor.main"], function () {
  const container = document.getElementById("container");
  const editorInstance = monaco.editor.create(container, {
    theme: "vs-dark",
    scrollbar: {
      vertical: "auto",
      horizontal: "auto",
    },
    minimap: { enabled: true },
    automaticLayout: true,
    value: python_code,
    language: "python",
  });
  const model = editorInstance.getModel();

  // - Configuration for the Constrained Editor : Starts Here
  const constrainedInstance = constrainedEditor(monaco);
  constrainedInstance.initializeIn(editorInstance);
  constrainedInstance.addRestrictionsTo(model, [
    {
      range: [1, 24, 1, 24], // Range of Util Variable name
      label: "utilName",
    },
    {
      range: [2, 35, 2, 35], // Range of Util Variable name
      label: "utilName1",
    },
    {
      range: [3, 1, 4, 1], // Range of Util Variable name
      label: "utilName2",
    },
    {
      range: [6, 17, 6, 17], // Range of Util Variable name
      label: "utilName3",
    },
    {
      range: [7, 63, 7, 63], // Range of Util Variable name
      label: "utilName4",
    },
    {
      range: [8, 9, 9, 1], // Range of Util Variable name
      label: "utilName5",
    },
    {
      range: [10, 17, 10, 17], // Range of Util Variable name
      label: "utilName6",
    },
    {
      range: [11, 77, 11, 77], // Range of Util Variable name
      label: "utilName7",
    },
    {
      range: [12, 9, 13, 1], // Range of Util Variable name
      label: "utilName8",
    },
    {
      range: [14, 17, 14, 17], // Range of Util Variable name
      label: "utilName9",
    },
    {
      range: [15, 85, 15, 85], // Range of Util Variable name
      label: "utilName10",
    },
    {
      range: [16, 9, 17, 1], // Range of Util Variable name
      label: "utilName10",
    },
  ]);
  // - Configuration for the Constrained Editor : Ends Here
});
