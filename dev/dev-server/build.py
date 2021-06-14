from pathlib import Path


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
    def __init__(self, docs_path: str) -> None:
        self.build_path = Path.joinpath(Path(__file__).resolve().parent, ".dev-build")
        self.docs_path = docs_path

    def build(self) -> str:
        pass
