import numpy as np
import domain
from domain import count, length, ratio


def tensor_generator(url):
    tensor = []
    tensor.append(len(url))
    tensor.append(domain.count.dots(url))
    tensor.append(domain.count.numbers(url))
    tensor.append(domain.count.vowels(url))
    tensor.append(domain.count.symbol(url))
    tensor.append(domain.length.max_between_dots(url))
    tensor.append(domain.length.avg_between_dots(url))
    tensor.append(domain.ratio.numbers_in_url(url))
    tensor.append(domain.ratio.symbol_in_url(url))
    tensor.append(domain.length.max_continuous_numbers(url))
    tensor.append(domain.length.max_continuous_vowels(url))
    tensor.append(domain.length.max_continuous_symbols(url))
    return tensor


def tensors_generator(urls):
    tensors = []
    for url in urls:
        tensors.append(tensor_generator(url))
    return tensors


url1 = 'www.qq.com'
url2 = 'www.baidu.com'
url3 = 'www.sogou.com'
url4 = 'www.bytedance.com'
url5 = 'music.qq.com'
urls = [url1, url2, url3, url4, url5]
tensors = tensors_generator(urls)


def tensor_format(tensors):
    records = tensors.shape[0]
    feature = tensors.shape[1]
    ruler = np.ptp(tensors, axis=0)
    minus = np.amin(tensors, axis=0)
    results = []
    for i in range(0, records):
        result = []
        for j in range(0, feature):
            if ruler[j] == 0:
                result.append(1)
                continue
            result.append((tensors[i][j] - minus[j]) / ruler[j])
        results.append(result)
    return np.array(results, dtype=float)


tensors = np.array(tensors)
print(tensors)
print('-----------------------------------------------------------------')
print(tensor_format(tensors))


import model

# print(np.array([tensor1, tensor2]))
