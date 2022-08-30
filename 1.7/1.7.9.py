from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        if type(number) != str:
            return False
        s = number.split('-')
        if len(s) != 4:
            return False
        if not all(map(lambda x: len(x) == 4, s)):
            return False
        return all(map(lambda x: x.isdigit(), s))


    @classmethod
    def check_name(cls, name):
        pass

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
print(is_number)

