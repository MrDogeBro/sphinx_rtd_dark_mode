from asyncio import run as async_run
from argparse import ArgumentParser
from pathlib import Path

from watch import Watcher


async def main():
    cwd = Path().cwd()

    parser = ArgumentParser()
    parser.add_argument("source_path")
    parser.add_argument("docs_path")
    args = parser.parse_args()

    source_path = Path.joinpath(cwd, args.source_path)
    docs_path = Path.joinpath(cwd, args.docs_path)

    watcher = Watcher(source_path, docs_path)
    watcher.watch()


if __name__ == "__main__":
    main()
