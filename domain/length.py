def max_between_dots(url):
    result = 0
    sub_list = list(url.split('.'))
    for sub in sub_list:
        if len(sub) > result:
            result = len(sub)
    return result


def avg_between_dots(url):
    result = 0
    count = 0
    sub_list = list(url.split('.'))
    for sub in sub_list:
        count = count + 1
        result = result + len(sub)
    result = result / count
    return result


def max_continuous_numbers(url):
    if len(url) == 0:
        return 0
    count = 0
    result = 0
    for index in range(0, len(url)):
        if index == 0:
            if url[index].isdigit():
                count = 1
                result = 1
        else:
            if url[index].isdigit():
                if url[index - 1].isdigit():
                    count = count + 1
                else:
                    count = 1
            else:
                count = 0

            if count >= result:
                result = count
    return result


def is_vowel(ch):
    if ch == 'a' or \
            ch == 'e' or \
            ch == 'i' or \
            ch == 'o' or \
            ch == 'u':
        return True
    return False


def max_continuous_vowels(url):
    if len(url) == 0:
        return 0
    url = url.lower()
    count = 0
    result = 0
    for index in range(0, len(url)):
        if index == 0:
            if is_vowel(url[index]):
                count = 1
                result = 1
        else:
            if is_vowel(url[index]):
                if is_vowel(url[index - 1]):
                    count = count + 1
                else:
                    count = 1
            else:
                count = 0

            if count >= result:
                result = count
    return result


def is_symbol(ch):
    if ch == '+' or \
            ch == '%' or \
            ch == '=' or \
            ch == '&' or \
            ch == '#' or \
            ch == '?':
        return True
    return False


def max_continuous_symbols(url):
    if len(url) == 0:
        return 0
    count = 0
    result = 0
    for index in range(0, len(url)):
        if index == 0:
            if is_symbol(url[index]):
                count = 1
                result = 1
        else:
            if is_symbol(url[index]):
                if is_symbol(url[index - 1]):
                    count = count + 1
                else:
                    count = 1
            else:
                count = 0

            if count >= result:
                result = count
    return result
