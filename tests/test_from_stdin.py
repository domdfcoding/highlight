# 3rd party

# 3rd party
from coincidence import AdvancedFileRegressionFixture
from consolekit.testing import CliRunner, Result, cli_runner
from domdf_python_tools.paths import PathPlus

# this package
from highlight.__main__ import main


def test_from_stdin(
		example_files: PathPlus,
		cli_runner: CliRunner,  # advanced_file_regression: AdvancedFileRegressionFixture,
		):
	result: Result = cli_runner.invoke(main, color=True, input=example_files.read_text())
	assert result.stdout
	# advanced_file_regression.check(result.stdout, extension=".md")

	assert result.exit_code == 0
