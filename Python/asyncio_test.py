import asyncio

async def async_compute(x,y):
    print("Computing %s + %s..." % (x,y))
    await asyncio.sleep(1)
    return x+y
async def print_sum(x,y):
    result = await async_compute(x,y)
    print("%s + %s = %s" % (x,y,result))

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(3,4))
    loop.close()