def dots(url):
    return url.count(".")


def numbers(url):
    return \
        url.count('0') + url.count('1') + url.count('2') + url.count('3') + url.count('4') + url.count('5') + \
        url.count('6') + url.count('7') + url.count('8') + url.count('9')


def vowels(url):
    return url.count('a') + url.count('e') + url.count('i') + url.count('o') + url.count('u')


def symbol(url):
    return url.count('+') + url.count('%') + url.count('=') + \
           url.count('&') + url.count('#') + url.count('?')

