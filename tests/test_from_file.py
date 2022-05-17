# stdlib
import shutil
from unittest import result

# 3rd party
from coincidence import AdvancedFileRegressionFixture
from consolekit.testing import CliRunner, Result
from consolekit.utils import coloured_diff
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.stringlist import StringList

# this package
from highlight.__main__ import main

referencefiles_dir = PathPlus(__file__).parent / "referencefiles"


def test_from_file(
		example_files: PathPlus,
		cli_runner: CliRunner,  # advanced_file_regression: AdvancedFileRegressionFixture,
		):
	reference_file_name = f"test_from_file_{example_files.name.replace('.', '_').replace('-', '_')}_.md"
	reference_file = referencefiles_dir / reference_file_name
	result: Result = cli_runner.invoke(main, args=[str(example_files)], color=True)
	assert result.stdout
	# if reference_file.exists():
	# 	output = StringList(result.stdout)
	# 	output.blankline(ensure_single=True)
	# 	coloured_diff(str(output), reference_file.read_text())
	# 	assert str(output) == reference_file.read_text()
	# else:
	# 	reference_file.write_clean(result.stdout)
	# 	raise AssertionError(f"Created reference file {reference_file_name!r}")
	# # advanced_file_regression.check(result.stdout, extension=".md")

	assert result.exit_code == 0


def test_from_file_no_extension(
		example_files: PathPlus,
		tmp_pathplus: PathPlus,
		cli_runner,  # advanced_file_regression: AdvancedFileRegressionFixture,
		):

	shutil.copyfile(example_files, tmp_pathplus / example_files.stem)

	reference_file_name = f"test_from_file_{example_files.name.replace('.', '_').replace('-', '_')}_.md"
	reference_file = referencefiles_dir / reference_file_name

	result: Result = cli_runner.invoke(main, args=[str(tmp_pathplus / example_files.stem)], color=True)
	assert result.stdout

	# if reference_file.exists():
	# 	output = StringList(result.stdout)
	# 	output.blankline(ensure_single=True)
	# 	coloured_diff(str(output), reference_file.read_text())
	# 	assert str(output) == reference_file.read_text()
	# else:
	# 	reference_file.write_clean(result.stdout)
	# 	raise AssertionError(f"Created reference file {reference_file_name!r}")

	# advanced_file_regression.check(result.stdout, extension=".md")

	assert result.exit_code == 0
