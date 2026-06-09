from backend.src.command.command import Command

class OrderController:
    def __init__(self):
        """I use this to hold whichever command should run next."""
        self.__command: Command | None = None

    def set_command(self, command: Command) -> None:
        """I use this to swap in the next command object."""
        self.__command = command

    def run_command(self) -> None:
        """I use this to execute the currently selected command if one exists."""
        if self.__command is not None:
            self.__command.execute()