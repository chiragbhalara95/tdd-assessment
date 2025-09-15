import re

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
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)

calc = StringCalculator()
print(calc.add(""))      # 0
print(calc.add("1"))     # 1
print(calc.add("1,5"))   # 6
print(calc.add("1,5,6"))   #12
print(calc.add("10,20,30,40,50"))   # 150
print(calc.add("1\n2,3"))    # 6
print(calc.add("//;\n1;2"))     # 3
print(calc.add("//|\n10|20|30")) # 60
print(calc.add("//.\n5.5.5"))   # 15
try:
    print(calc.add("1,-2,3,-4"))
except ValueError as e:
    print(e)  # negative numbers not allowed -2,-4
