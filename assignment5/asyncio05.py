from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(menu):
    # generate a random value between 0 and 1
    value = 1+random()
    # block for a moment
    print(f'>Microwave ({menu}) : Cooking {value} sceounds...')
    await asyncio.sleep(value)
    print(f"Microwave ({menu}) Finnished cooking")
    # report the value
    return menu, value

# main coroutine
async def main():
    menu = ['rice','noodle','curry']
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in menu]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report results
    print(f"Completed task: {len(done)} task")
    menu, value = await done.pop()
    print(f'- {menu} is completed in {value}')
    print(f"Uncompleted task: {len(pending)} task")
    
# start the asyncio program
asyncio.run(main())