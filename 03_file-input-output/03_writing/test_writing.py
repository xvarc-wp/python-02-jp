from pathlib import Path


class TestWriting:
    path_to_target = "./words_reverse.txt"
    path_to_original = "../words.txt"

    def test_if_file_exists(self):
        path = Path(self.path_to_target)

        assert path.is_file()

    def test_if_contents_match(self):
        with (
            open(self.path_to_target) as actual_file,
            open(self.path_to_original) as original_file,
        ):
            actual_outputs = actual_file.readlines()
            expected_outputs = original_file.readlines()

            assert len(actual_outputs) == len(expected_outputs)

            for i, actual_output in enumerate(actual_outputs):
                j = len(actual_outputs) - i - 1
                assert actual_output.strip() == expected_outputs[j].strip()
