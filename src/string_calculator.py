import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        parts = re.split(r"[,\n]", numbers)
        return sum(int(part) for part in parts)

calc = StringCalculator()
print(calc.add(""))      # 0
print(calc.add("1"))     # 1
print(calc.add("1,5"))   # 6
print(calc.add("1,5,6"))   #12
print(calc.add("10,20,30,40,50"))   # 150
print(calc.add("1\n2,3"))    # 6
