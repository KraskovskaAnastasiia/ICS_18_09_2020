class StrChild(str):

    def replies_of_queue(self, s):
        for id, char in enumerate(s):
            if(id <= len(s)-2):
                if(char == s[id+1] and char == s[id+2]):
                    return True

        return False

    def is_palindrom(self, raw):
        if(raw == ''):
            return True

        reversed_raw = raw[::-1]

        if(reversed_raw == raw):
            return True
        else:
            return False



replies_test_str = "Just Be Yourself"
no_replies_test_str = "Life Is Good"

palindrom_test = "Live. Love. Enjoy"
no_palindrom_test = "Enjoy Your Life"

my_str = StrChild()
print(my_str.replies_of_queue(replies_test_str))
print(my_str.replies_of_queue(no_replies_test_str))
print("\n")
print(my_str.is_palindrom(palindrom_test))
print(my_str.is_palindrom(no_palindrom_test))