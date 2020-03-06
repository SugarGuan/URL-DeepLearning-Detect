from domain import count


def numbers_in_url(url):
    if len(url) == 0:
        return 0
    numbers = count.numbers(url)
    result = numbers / len(url)
    return result


def symbol_in_url(url):
    if len(url) == 0:
        return 0
    symbols = count.symbol(url)
    result = symbols / len(url)
    return result
