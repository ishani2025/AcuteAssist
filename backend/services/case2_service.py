import asyncio

async def fetch_hospital_a(aadhaar):
    return {}

async def fetch_hospital_b(aadhaar):
    return {}

async def fetch_hospital_c(aadhaar):
    return {}

async def fetch_fragmented_history(aadhaar):

    results = await asyncio.gather(
        fetch_hospital_a(aadhaar),
        fetch_hospital_b(aadhaar),
        fetch_hospital_c(aadhaar)
    )

    merged = {}

    for r in results:
        merged.update(r)

    return merged