import asyncio
from twikit import Client

USERNAME = 'DevinLave43610'
EMAIL = 'devinlave02@gmail.com'
PASSWORD = 'CMSC396HProject'

# Initialize client
client = Client(user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36', language ='en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

asyncio.run(main())