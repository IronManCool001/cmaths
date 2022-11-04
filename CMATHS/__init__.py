from .add import add
from .product import product

__version__ = "0.1.0"
__author__ = 'Debaditya Malakar'

if __name__ == "__main__":
    print(add(product(2,3),product(3,4)))