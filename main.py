from typing import List
import asyncio
import time
import aiofiles
from tqdm.asyncio import tqdm
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    full_name: str = None


async def get_batch_from_file(file_name: str, chunk_size: int = 1000):
    async with aiofiles.open(file_name, mode="r") as file:
        while True:
            lines = await file.readlines(chunk_size)
            if not lines:
                break
            yield lines


async def process_batch(batch: List[str]) -> List[str]:
    # the batch itself should also be concurrently processed
    processed_lines = await asyncio.gather(*[process_line(line) for line in batch])
    return processed_lines


async def process_line(line: str) -> str:
    fields = line.strip().split(",")
    user = {
        "id": fields[0],
        "username": fields[1],
        "email": fields[2],
        "is_active": fields[3].lower() == "true",
        "full_name": fields[4],
    }

    await asyncio.sleep(0.2)  # simulating a network call
    return User(**user).model_dump_json() + "\n"


async def write_batch(batch: List[str], filename: str):
    async with aiofiles.open(filename, "a") as file:
        await file.writelines(batch)


async def count_lines(filename: str) -> int:
    count = 0
    async with aiofiles.open(filename, "r") as file:
        async for _ in file:
            count += 1
    return count


async def main():
    stime = time.time()

    write_semaphore = asyncio.Semaphore(5)
    batch_size = 100000

    pbar = tqdm(
        desc="Processing",
        unit="lines",
        ncols=100,
        ascii=True,
        dynamic_ncols=True,
    )
    read_lines_count = 0
    async for batch in get_batch_from_file("users.txt", batch_size):
        read_lines_count += len(batch)
        pbar.update(
            len(batch)
        )  # update progress bar with number of lines processed in this batch
        processed_batch = await process_batch(batch)
        # Use the semaphore here to limit the number of concurrent writes
        async with write_semaphore:
            await write_batch(processed_batch, "processed_users.txt")

    pbar.close()
    etime = time.time()
    print(f"[*] Processing file took {etime-stime} seconds.")


if __name__ == "__main__":
    asyncio.run(main(), debug=False)
