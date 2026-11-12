# verify_postgres.py
import asyncio

import asyncpg
import psycopg2

DSN = "postgresql://learner:wh1rLw!nd23@localhost:5432/python_course"

# Synchronous driver
with psycopg2.connect(DSN) as conn, conn.cursor() as cur:
    cur.execute("SELECT version();")
    print("psycopg2 →", cur.fetchone()[0][:40])


# Asynchronous driver
async def main() -> None:
    conn = await asyncpg.connect(DSN)
    print("asyncpg  →", await conn.fetchval("SELECT current_database()"))
    await conn.close()


asyncio.run(main())
