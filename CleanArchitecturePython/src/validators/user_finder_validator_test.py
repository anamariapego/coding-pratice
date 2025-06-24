from .user_finder_validator import user_finder_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_user_finder_validator():
    print()
    request = MockRequest()
    request.args = {"first_name": "meuNome"}

    user_finder_validator(request)
