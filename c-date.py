from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%B %d %Y, %H:%M")
print(dt_string)
