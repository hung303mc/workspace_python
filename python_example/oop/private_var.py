class MyClass:
    def __init__(self):
        self.myvar = 1       # public
        self._myvar = 2      # meant for internal use (private). 'Please' don't access directly
        self.__myvar = 3     # name mangling
        self.__myvar_ = 4    # name mangling
        self.__myvar__ = 5   # magic attribute

    def print(self):
        # All variables can be used within the class definition
        print(self.myvar)
        print(self._myvar)
        print(self.__myvar)
        print(self.__myvar_)
        print(self.__myvar__)

if __name__ == '__main__':
    myinstance1 = MyClass()
    print(myinstance1.myvar)
    print(myinstance1._myvar)
    # Variables beginning with __ are not accessible outside the class except those ending with __
    print(myinstance1.__myvar)    # AttributeError
    print(myinstance1.__myvar_)   # AttributeError
    print(myinstance1.__myvar__)

    myinstance1.print()

    print(dir(myinstance1))
    # ['_MyClass__myvar', '_MyClass__myvar_', '__myvar__', '_myvar', ...]
    # Variables beginning with __ are renamed by prepending with an underscore and classname (called name mangling)