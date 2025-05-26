def is_valid_string(string: str) -> bool:
    for i, c in enumerate(string):
        if c.isdigit():
            if i == 0:
                asterisk_count = int(string[i + 1] == "*")
            elif i == len(string) - 1:
                asterisk_count = int(string[i - 1] == "*")
            else:
                asterisk_count = int(string[i - 1] == "*")
                asterisk_count += int(string[i + 1] == "*")

            if asterisk_count != int(c):
                return False
    
    return True


if __name__ == "__main__":
    print(is_valid_string("***"))
    print(is_valid_string("111"))
    print(is_valid_string("000"))
    print(is_valid_string("0*1"))
    print(is_valid_string("1*1"))