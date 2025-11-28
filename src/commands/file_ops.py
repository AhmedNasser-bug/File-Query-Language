from .interface import ICommand

class CreateCommand(ICommand):
    def __init__(self, path: str, content: str = ""):
        self.path = path
        self.content = content

    def validate(self) -> bool:
        return len(self.path) > 0

    def execute(self) -> str:
        # TODO: Implement file creation
        return f"Created file: {self.path}"
