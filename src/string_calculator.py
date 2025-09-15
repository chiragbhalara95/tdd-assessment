import re

class NegativesError(ValueError):
    """Raised when one or more negative numbers are passed to add()."""
    pass

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = r"[,\n]"  # default delimiters

        # Custom delimiter syntax
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            delimiter_spec = delimiter_line[2:]

            # Check for bracketed delimiters
            bracketed = re.findall(r"\[(.*?)\]", delimiter_spec)
            if bracketed:
                # Combine multiple delimiters with |
                delimiter = "|".join(re.escape(d) for d in bracketed)
            else:
                delimiter = re.escape(delimiter_spec)

        parts = re.split(delimiter, numbers)
        nums = [int(part) for part in parts if part]

        # Find negative numbers
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise NegativesError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)
