class Foo:
    first_is_called = False
    second_is_called = False
    
    def __init__(self):
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_is_called = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.first_is_called is False:
            pass
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_is_called = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.second_is_called is False:
            pass
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
