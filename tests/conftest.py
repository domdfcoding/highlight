# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus

pytest_plugins = ("coincidence", "consolekit.testing")

examplefiles_dir = PathPlus(__file__).parent / "examplefiles"


@pytest.fixture(
		params=(
				pytest.param(file, id=file.name)
				for file in sorted(list(examplefiles_dir.iterchildren()))
				if file.is_file()
				),
		)
def example_files(request):
	yield request.param
