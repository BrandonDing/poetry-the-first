"""This is a test file"""
def hello() -> str:
    """Summary line.

    Extended description of function.

    Args:
        hello (str): Description of arg1

    Returns:
        str: Description of return value
    """

    return "hello"


if __name__ == "__main__":  # pragma: no cover
    print(hello())
