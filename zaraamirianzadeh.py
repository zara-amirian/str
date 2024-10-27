class CustomStr:
    def __init__(self, value):
        self.value = value
    def remove_duplicate(self):
        result = []
        for char in self.value:
            if char not in result:
                result.append(char)
        return ''.join(result)
    def custom_split(self, delimiter=' '):
        return self.value.split(delimiter)
    def is_float(self):
        try:
            float(self.value)
            return True
        except ValueError:
            return False
    def set_value(self, new_value):
        self.value = new_value
    def is_palindrome(self):
        filtered_value = ''.join(filter(str.isalnum, self.value)).lower()
        return filtered_value == filtered_value[::-1]
custom_string = CustomStr("Zahra Amirian Zadeh")
print(custom_string.custom_split())
print(custom_string.remove_duplicate())
print(custom_string.is_float())
print(custom_string.is_palindrome())