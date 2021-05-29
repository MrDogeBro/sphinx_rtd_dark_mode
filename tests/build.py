import os
import unittest
from tempfile import TemporaryDirectory


class TestBuild(unittest.TestCase):
    def test_build(self):
        with TemporaryDirectory() as temp_dir:
            src_dir = os.path.join(os.path.dirname(__file__), "test-build")
            output_dir = os.path.join(temp_dir, "build")

            build_output = os.system(
                "sphinx-build -b html {} {}".format(src_dir, output_dir)
            )

        self.assertEqual(build_output, 0)


if __name__ == "__main__":
    unittest.main()
