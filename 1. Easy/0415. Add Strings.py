class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)

        numero1 = int(num1)
        numero2 = int(num2)

        return str(numero1 + numero2)
