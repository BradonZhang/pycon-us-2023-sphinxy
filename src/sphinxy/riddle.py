from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    """Dataclass representing a riddle."""

    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Checks if the answer to the riddle is correct.

        Args:
            answer (str): The user's answer.

        Returns:
            bool: Whether the answer to the riddle is correct.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Gets a hint iterator.

        Yields:
            Iterator[str]: A stream of hints for the riddle.
        """
        yield from iter(self.answer)
