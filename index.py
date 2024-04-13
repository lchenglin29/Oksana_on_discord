from main import main
import keep_alive
import asyncio

keep_alive.keep_alive()
asyncio.run(main())