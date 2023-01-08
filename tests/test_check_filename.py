import pytest
from check_filename import check_filename_prefix, main


@pytest.mark.parametrize(
    "filename, prefix_list, expected",
    [
        ("ops_file_1", ["ops_", "job_"], 0),
        ("job_file_1", ["ops_", "job_"], 0),
        ("folder/job_file_1", ["ops_", "job_"], 0),
        ("folder/job_file_2.py", ["ops_", "job_"], 0),
        ("folder1/folder2/job_file_2.py", ["ops_", "job_"], 0),
        ("Ops_file_1", ["ops_", "job_"], 1),
        ("Job_file_1", ["ops_", "job_"], 1),
        ("ups_file_1", ["ops_", "job_"], 1),
        ("folder1/folder2/Job_file_2.py", ["ops_", "job_"], 1),
    ],
)
def test_01_check_filename_prefix(filename, prefix_list, expected):
    result = check_filename_prefix(filename, prefix_list)
    assert result == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            [
                "--allowed_prefix=ops_",
                "--allowed_prefix=job_",
                "ops_file_1",
                "job_file_1",
            ],
            0,
        ),
        (
            [
                "--allowed_prefix=ops_",
                "--allowed_prefix=job_",
                "Ops_file_1",
                "Job_file_1",
                "ups_file_1",
            ],
            1,
        ),
    ],
)
def test_01_main(args, expected):
    result = main(args)
    assert result == expected
