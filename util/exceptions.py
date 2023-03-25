class InvalidVerbosityConfigurationException(Exception):
    def __init__(self) -> None:
        self.messages = "Cannot be both quiet and verbose"

    def __str__(self) -> str:
        return f"ERROR: {self.messages}"

class InvalidInstallTypeException(Exception):
    def __init__(self, message: str) -> None:
        self.messages = f"Invalid install type provided: {message}"

    def __str__(self) -> str:
        return f"ERROR: {self.messages}"
