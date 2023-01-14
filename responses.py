import random

from datetime import datetime
import time 
now = datetime.now()
hrs = now.hour
print('Datetime is:', now)
day = now.strftime('%A'))

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    return 'I didn\'t understand what you wrote. Try typing "!help".'
def get_intresponse(message:int) -> int:
    
    
