from sphinxy.riddle import Riddle


class IncorrectAnswer(Exception):
    """Exception for incorrect answer."""


class Sphinx:
    """Class representing a Sphinx, who prompts the user with a riddle.

    Args:
        name (str): The name of the Sphinx.
    """

    def __init__(self, name: str):
        self._name = name
        self._riddle = Riddle(
            question=(
                "What goes on four legs in the morning, two legs at noon, "
                "and three legs in the evening?"
            ),
            answer="man",
        )

    def introduce(self) -> str:
        """Provides the introduction text for the Sphinx.

        Returns:
            str: The Sphinx's introduction text.
        """
        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        """Updates the riddle the Sphinx asks.

        Args:
            riddle (Riddle): The updated riddle the Sphinx asks.

        Returns:
            str: A message from the Sphinx indicating that the riddle has changed.
        """
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str | None]:
        """Poses the riddle to the user.

        Args:
            include_hint (bool, optional): Whether to include the question hint.
            Defaults to False.

        Returns:
            tuple[str, str | None]: A tuple of the riddle question and its hint (if
            applicable).
        """
        hint = (
            f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            if include_hint
            else None
        )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        """Evaluates the given answer to the riddle.

        Args:
            answer (str): The given answer to the riddle.
            return_hint (bool, optional): Controls whether a hint for the riddle should
                be returned. Defaults to False.

        Raises:
            IncorrectAnswer: Exception for incorrect answer.

        Returns:
            str: The result of the evaluation of the answer.
        """
        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")
