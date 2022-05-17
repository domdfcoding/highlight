# stdlib
import shutil
from typing import List

# 3rd party
import pytest
from coincidence import AdvancedFileRegressionFixture
from consolekit.testing import CliRunner, Result
from domdf_python_tools.paths import PathPlus

# this package
from highlight.__main__ import main

examplefiles_dir = PathPlus(__file__).parent / "examplefiles"


@pytest.mark.parametrize(
		"extra_args",
		[
				pytest.param(["--show-tabs"], id="show_tabs"),
				pytest.param(["-T"], id="show_tabs_short"),
				pytest.param(["--show-ends"], id="show_ends"),
				pytest.param(["-E"], id="show_ends_short"),
				pytest.param(["--number"], id="number"),
				pytest.param(["-n"], id="number_short"),
				pytest.param(["-T", "--show-ends"], id="tabs_and_ends"),
				pytest.param(["--number", "-E"], id="number_and_ends"),
				pytest.param(["-n", "-E", "--show-tabs"], id="all"),
				]
		)
def test_options(
		cli_runner: CliRunner,
		advanced_file_regression: AdvancedFileRegressionFixture,
		extra_args: List[str],
		):

	for file in sorted(list(examplefiles_dir.iterchildren())):
		if file.is_file():

			result: Result = cli_runner.invoke(main, args=[str(file), *extra_args], color=True)
			advanced_file_regression.check(result.stdout, extension=f"{file.name}.md")

	assert result.exit_code == 0
