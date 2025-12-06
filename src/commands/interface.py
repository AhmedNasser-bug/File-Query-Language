from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def command(tokens:list):
        """Factory method to create command instance from tokens."""
        pass

    @abstractmethod
    def validate(self) -> bool:
        """Check if command arguments are valid before execution."""
        pass

    @abstractmethod
    def execute(self) -> str:
        """Run the command and return output string."""
        pass
