from distutils.dir_util import copy_tree, remove_tree
from os import chdir
from pathlib import Path
from subprocess import run as run_cmd, PIPE
from tempfile import TemporaryDirectory
from time import sleep


class BuildOutput:
    def __init__(self, traceback: str, status: int) -> None:
        self.traceback = traceback
        self.status = status

    @property
    def traceback(self) -> str:
        return self.traceback

    @property
    def status(self) -> int:
        return self.status


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

        build_source_path = str(Path.joinpath(self.output_path, "source"))
        build_docs_path = str(Path.joinpath(self.output_path, "docs"))

        remove_tree(self.output_path)

        copy_tree(self.source_path, build_source_path)
        copy_tree(self.docs_path, build_docs_path)

        build_cmd = run_cmd(
            ["sphinx-build", "docs", "build"],
            stdout=PIPE,
            cwd=str(self.output_path),
        )

        build_traceback = build_cmd.stdout.decode("utf-8")
        self.in_progress = False

        return BuildOutput(build_traceback, build_cmd.returncode)
