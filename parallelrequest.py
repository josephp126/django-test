import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer

START_TIME = default_timer()

def fetch(session, csv):
    base_url = "http://localhost:8000"
    with session.post(base_url) as response:
        data = response.text
        if response.status_code != 200:
            print("FAILURE::{0}".format(url))

        elapsed = default_timer() - START_TIME
        time_completed_at = "{:5.2f}s".format(elapsed)
        print("{0:<30} {1:>20}".format(csv, time_completed_at))

        return data

async def get_data_asynchronous():
    print("{0:<30} {1:>20}".format("File", "Completed at"))
    with ThreadPoolExecutor(max_workers=70) as executor:
        with requests.Session() as session:
            # Set any session parameters here before calling `fetch`
            loop = asyncio.get_event_loop()
            START_TIME = default_timer()
            tasks = [
                loop.run_in_executor(
                    executor,
                    fetch,
                    *(session, x) # Allows us to pass in multiple arguments to `fetch`
                )
                for x in range(50)
            ]
            for response in await asyncio.gather(*tasks):
                pass

def main():
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_data_asynchronous())
    loop.run_until_complete(future)

main()