import asyncio
from twikit import Client

USERNAME = 'DevinLave43610'
EMAIL = 'devinlave02@gmail.com'
PASSWORD = 'CMSC396HProject'

# Initialize client
client = Client(
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
)

async def main():
    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )
    
    print(await client.get_trends('trending'))

asyncio.run(main())