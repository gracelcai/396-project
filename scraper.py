import asyncio
from twikit import Client

USERNAME = 'DevinLave43610'
EMAIL = 'devinlave02@gmail.com'
PASSWORD = 'CMSC396HProject'

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

asyncio.run(main())