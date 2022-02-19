from ctypes import util
import utility
from utility import multiply, divide
from shopping.more_shopping import shopping_cart

if __name__ == '__main__':
    print(shopping_cart.buy("apple"))
    print(divide(5, 2))
    print(multiply(5, 2))
    print(max([1, 2, 3]))


print(type(utility.st1))