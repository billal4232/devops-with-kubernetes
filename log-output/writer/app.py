import uuid
from datetime import datetime
import time

random_string = str(uuid.uuid4())

while True:
    now = datetime.now()
    with open("/usr/src/app/files/output.txt", "w") as f:
        f.write(f"{now}: {random_string}\n")
    time.sleep(5)