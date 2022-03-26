from src.adapters.controllers.example_controller import ExampleController
from src.main.subjects.module import Module,Modular


class Test_Module:

    def test_module_working(self):
        controller = Modular.getInject(ExampleController)
        assert isinstance(controller,ExampleController)