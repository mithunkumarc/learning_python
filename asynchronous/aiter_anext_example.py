import asyncio

# Asyc Iterable object should implement __aiter__ and __anext__ methods
# aiter and anext are used to iterate/read values from Async iterable
class AsynIterator():
    def __init__(self) -> None:
        self.counter = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.counter >= 10:
            raise StopAsyncIteration
        self.counter += 1
        return self.counter

async def main():
    it = AsynIterator()
    awaitable = anext(it)
    result = await awaitable
    print("using anext() : ",result) # reading only one element
    # rest of the elments read by aiter()
    async for element in aiter(it):
        if element:
            print("using aiter() : ",element)
        else:
            print("No element")

asyncio.run(main())
