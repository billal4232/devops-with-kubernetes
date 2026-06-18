import uuid
from datetime import datetime
import time

random_string = str(uuid.uuid4())

while True:
    now = datetime.now()
    print(f"{now}: {random_string}")
    time.sleep(5)