import domain
from domain import count


def tensor_generator(url):
    tensor = []
    tensor.append(domain.length(url))
    tensor.append(domain.count.dots(url))
    tensor.append(domain.count.numbers(url))
    tensor.append(domain.count.vowels(url))
    tensor.append(domain.count.symbol(url))
    return tensor


url1 = 'www.qq.com'
url2 = 'www.baidu.com'

tensor1 = tensor_generator(url1)
print(tensor1)



