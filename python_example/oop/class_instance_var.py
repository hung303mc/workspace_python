class MyClass:
    count = 0  # Total number of instances
               # A class variable shared by all the instances

    def __init__(self):
        # Update class variable
        self.__class__.count += 1   # Increment count
                                    # or MyClass.count += 1
        # Create instance variable: an 'id' of the instance in running numbers
        self.id = self.__class__.count

    def get_id(self):
        return self.id

    def get_count(self):
        return self.__class__.count

if __name__ == '__main__':
    print(MyClass.count)                # 0
    
    myinstance1 = MyClass()
    print(MyClass.count)                # 1
    print(myinstance1.get_id())         # 1
    print(myinstance1.get_count())      # 1
    print(myinstance1.__class__.count)  # 1
    
    myinstance2 = MyClass()
    print(MyClass.count)                # 2
    print(myinstance1.get_id())         # 1
    print(myinstance1.get_count())      # 2
    print(myinstance1.__class__.count)  # 2
    print(myinstance2.get_id())         # 2
    print(myinstance2.get_count())      # 2
    print(myinstance2.__class__.count)  # 2
