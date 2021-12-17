import pytest

# У нас есть набор тестов, который использует несколько фикстур.
# Посчитайте, сколько смайликов будет напечатано при выполнении этого тестового класса?

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print("bla")

    def test_second_smiling_faces(self, prepare_faces):
         print("bla")

# The answer is:  5