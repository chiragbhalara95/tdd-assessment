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
        return sum(int(part) for part in parts)

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
