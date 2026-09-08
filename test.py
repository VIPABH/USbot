import random, asyncio
from ABH import *
COMMAND_FORMATS = [
    "تقييد عام {time} {user}",
    "تقييد عام {user} {time}"  
]
def send_random_restrict_command():
    chosen_format = random.choice(COMMAND_FORMATS)    
    command_text = chosen_format.format(user=random.choice(['@iu_abh ', 7811364724]), time=random.choice([20, 300, 400, 999, 12399, 1, random.randint(1, 1000)]))
    return command_text
@ABH.on(events.NewMessage(pattern=r'^تجربة$', outgoing=True))
async def test(e):
    for _ in range(25):
        text = send_random_restrict_command()
        await e.respond(text)
        await asyncio.sleep(0.25)
