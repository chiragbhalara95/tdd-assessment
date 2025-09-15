import re
class NegativesError(ValueError):
    """Raised when one or more negative numbers are passed to add()."""
    pass

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = r"[,\n]"  # default delimiters

        # Check for custom delimiter syntax: //{delimiter}\n
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            delimiter = re.escape(delimiter_line[2:])  # escape special chars like *

        parts = re.split(delimiter, numbers)
        nums = [int(part) for part in parts if part]

        # Find negative numbers
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise NegativesError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)

