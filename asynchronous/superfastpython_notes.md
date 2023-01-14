https://superfastpython.com/python-asyncio/

#### coroutine

        A coroutine can be wrapped in an asyncio.Task object and executed independently, as opposed to being executed directly within a coroutine. 
        The Task object provides a handle on the asynchronously execute coroutine.


#### cpu vs io

        In the case of a CPU-bound operation, it would complete faster if our CPU was
        more powerful, for instance by increasing its clock speed from 2 GHz to 3 GHz. In the
        case of an I/O-bound operation, it would get faster if our I/O devices could handle
        4 CHAPTER 1 Getting to know asyncio
        more data in less time. This could be achieved by increasing our network bandwidth
        through our ISP or upgrading to a faster network card

#### example 1

        import asyncio
        # below function, you can call using asyncio.run() or using await in another function
        async def hello_world_message() -> str:
         await asyncio.sleep(1)
         return ‘Hello World!’
        
        async def main() -> None:
         message = await hello_world_message()
         print(message)
        asyncio.run(main())
        

#### event loop and task

      when we call a coroutine directly, we don’t put it on the event loop
      to run. Instead, we get a coroutine object that we then need to either use the await
      keyword on it or pass it in to asyncio.run to run and get a value. With only these tools
      we can write async code, but we can’t run anything concurrently. To run coroutines
      concurrently, we’ll need to introduce tasks.

       Tasks are wrappers around a coroutine that schedule a coroutine to run on the
      event loop as soon as possible. This scheduling and execution happen in a non-blocking
      fashion, meaning that, once we create a task, we can execute other code instantly
      while the task is running. This contrasts with using the await keyword that acts in a
      blocking manner, meaning that we pause the entire coroutine until the result of the
      await expression comes back.
       The fact that we can create tasks and schedule them to run instantly on the event
      loop means that we can execute multiple tasks at roughly the same time. When these
      tasks wrap a long-running operation, any waiting they do will happen concurrently

-------------------------

#### Once we have a task object, we can put it in an await expression that will extract the return value once it is complete.

      import asyncio
      from util import delay
      async def main():
       sleep_for_three = asyncio.create_task(delay(3))
       print(type(sleep_for_three))
       result = await sleep_for_three
       print(result)
      asyncio.run(main())

#### use asyncio task to call coroutine as it runs on event loop 

      and increase performance and you an manage/monitor task also 


#### cancel task : use helper for cancelling asyncio.wait_for , using timeout not easy way

        import asyncio
        from asyncio import CancelledError
        from util import delay
        async def main():
         long_task = asyncio.create_task(delay(10))
         seconds_elapsed = 0
         while not long_task.done():
         print('Task not finished, checking again in a second.')
         await asyncio.sleep(1)
         seconds_elapsed = seconds_elapsed + 1
         if seconds_elapsed == 5:
         long_task.cancel()
         try:
         await long_task
         except CancelledError:
         print('Our task was cancelled')
        asyncio.run(main())

#### asyncio.wait_for 

        import asyncio
        from util import delay
        async def main():
         delay_task = asyncio.create_task(delay(2))
         try:
         result = await asyncio.wait_for(delay_task, timeout=1)
         print(result)
         except asyncio.exceptions.TimeoutError:
         print('Got a timeout!')
         print(f'Was the task cancelled? {delay_task.cancelled()}')
        asyncio.run(main())
----------------------------------------

#### asyncio.shield : This function will prevent cancellation of the coroutine we pass in, giving it a “shield,” which cancellation requests then ignore.

        import asyncio
        from util import delay
        async def main():
         task = asyncio.create_task(delay(10))
         try:
         result = await asyncio.wait_for(asyncio.shield(task), 5)
         print(result)
         except TimeoutError:
         print("Task took longer than five seconds, it will finish soon!")
         result = await task
         print(result)
        asyncio.run(main())

#### awaitables

        anything that implements the
        __await__ method can be used in an await expression. Coroutines inherit directly
        from Awaitable, as do futures. Tasks then extend futures, 
        which gives us the inheritance.

        awaitable   -> coroutine 
              -> future -> tasks


#### cpu bound tasks 

        for 1 -> 1000 ,calling this using task (multiple) : still works asynchronously as it is 
        cpu bound task 

        happens same for calling(multiple) api (url) : blocking


#### without using task you can create event loop manually 


        import asyncio
        def call_later():
         print("I'm being called in the future!")
        Listing 2.21 Manually creating the event loop
        Listing 2.22 Accessing the event loop
        Using debug mode 47
        async def main():
         loop = asyncio.get_running_loop()
         loop.call_soon(call_later)
         await delay(1)
        asyncio.run(main())

