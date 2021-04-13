# Iterator 

# Iterator allows traversing the elements of collections 
# without exposing the internal details. 

# Use case. Provide a standard way of traversing the collections.

# + clean client code (Single Responsability Principle).

# + Introducing iterators in collections is possible without changing 
# the client's code (Open/Closed Principle)

# + Each iteration object has its own iteration state, so you can 
# delay & continue iteration 

# - Use of iterators with simple collections can overload the application

from __future__ import annotations


from collections.abc import Iterable, Iterator
from typing import Any, List

class AlphabeticalOrderIterator(Iterator):
    _position: int = None 
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        
        return value 

class WordsCollection(Iterable):

    def __init__(self, collection: List[Any] = []):
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)













# Steate
# State helps an object to alter its behavior in case its internal state changes.

#Use case. State helps me
#   . Alter the enormous number of object states.
#   . Reduce the number of lines with duplicate code in similar transitions & states.
#   . Avoid massive conditionals 

# + Follows Single Responsability principle: separate classes for the code related to a different state.
# + Doesn't change the context or state of classes when adding new states (Open/Closed Principle)
# - Using State can be too much in case the state machine isn't almost changing.

from abc import abstractclassmethod, ABC

class Context(ABC):
    _state = None 

    def __init__(self, state: State):
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f'Context: Transition to {type(state).__name__}')
        self._state = state 
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

class State(ABC):

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context 

    @abstractclassmethod
    def handle1(self):
        pass 

    @abstractclassmethod
    def handle2(self):
        pass


class ConcreteStateA(State):

    def handle1(self):
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())


    def handle2(self):
        print("ConcreteStateA handles request2.")

class ConcreteStateB(State):
    def handle1(self):
        print("ConcreteStateB handles request1.")

    def handle2(self):
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())





if __name__ == '__main__':

    '''
    # Iterator pattern test

    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()))
    '''

    # State patter test

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()