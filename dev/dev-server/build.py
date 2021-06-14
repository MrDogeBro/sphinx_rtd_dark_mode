from distutils.dir_util import copy_tree, remove_tree
from distutils.errors import DistutilsFileError
from os import chdir
from pathlib import Path
from subprocess import run as run_cmd
from tempfile import TemporaryDirectory
from time import sleep


class BuildOutput:
    def __init__(self, traceback: str, status: int) -> None:
        self.traceback = traceback
        self.status = status


class Builder:
    def __init__(self, source_path: str, docs_path: str) -> None:
        self.output_path = Path.joinpath(
            Path(__file__).resolve().parent, "../.dev-build"
        )
        self.source_path = source_path
        self.docs_path = docs_path
        self.in_progress = False

    def build(self) -> BuildOutput:
        if self.in_progress:
            return

        self.in_progress = True

        with TemporaryDirectory() as temp_dir:
            build_source_path = str(
                Path.joinpath(Path(temp_dir), "sphinx_rtd_dark_mode")
            )
            build_docs_path = str(Path.joinpath(Path(temp_dir), "docs"))
            build_output_path = str(Path.joinpath(Path(temp_dir), "build"))
            output_build_path = Path.joinpath(self.output_path, "build")

            if Path(output_build_path).exists():
                remove_tree(output_build_path)

            try:
                copy_tree(self.source_path, build_source_path)
                copy_tree(self.docs_path, build_docs_path)
            except DistutilsFileError:
                return BuildOutput(
                    "Error in file copy. You are probably fine to ignore this error and continue as it is most likely a bug.",
                    1,
                )

            build_cmd = run_cmd(
                ["sphinx-build", "docs", "build"], cwd=temp_dir, capture_output=True
            )

            if build_cmd.returncode > 1:
                return BuildOutput(
                    build_cmd.stderr.decode("utf-8"), build_cmd.returncode
                )

            copy_tree(build_output_path, str(output_build_path))

        self.in_progress = False

        return BuildOutput(build_cmd.stdout.decode("utf-8"), build_cmd.returncode)
