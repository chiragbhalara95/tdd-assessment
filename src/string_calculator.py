class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        parts = numbers.split(",")
        return sum(int(part) for part in parts)

# calc = StringCalculator()
# print(calc.add(""))      # 0
# print(calc.add("1"))     # 1
# print(calc.add("1,5"))   # 6
