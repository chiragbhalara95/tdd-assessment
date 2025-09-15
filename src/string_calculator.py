class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        parts = numbers.split(",")
        return sum(int(part) for part in parts)

calc = StringCalculator()
# print(calc.add(""))      # 0
# print(calc.add("1"))     # 1
# print(calc.add("1,5"))   # 6
# print(calc.add("1,5,6"))   #12
# print(calc.add("10,20,30,40,50"))   # 150
