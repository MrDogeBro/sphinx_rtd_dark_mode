from pathlib import Path


class Builder:
    def __init__(self, docs_path: str) -> None:
        self.build_path = Path.joinpath(Path(__file__).resolve().parent, ".dev-build")
        self.docs_path = docs_path

    def build(self) -> str:
        pass
