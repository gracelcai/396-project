import asyncio
from twikit import Client

USERNAME = 'DevinLave43610'
EMAIL = 'devinlave02@gmail.com'
PASSWORD = 'CMSC396HProject'

# Initialize client

client = Client(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36')
async def login():
    if os.path.exists(cookie_file):
        client.load_cookies(cookie_file)
    else:
        await client.login(
            auth_info_1=username,
            auth_info_2=email,
            password=password
        )
        client.save_cookies(cookie_file)

    asyncio.run(main())