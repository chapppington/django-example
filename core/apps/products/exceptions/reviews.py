from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class ReviewException(ServiceException):
    @property
    def message(self) -> str:
        return "Review exception occurred"


@dataclass(eq=False)
class ReviewInvalidRatingException(ReviewException):
    rating: int

    @property
    def message(self) -> str:
        return f"Invalid rating: {self.rating}, must be between 1 and 5"
