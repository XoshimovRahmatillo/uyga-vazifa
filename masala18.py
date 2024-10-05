from datetime import datetime, timedelta

sana = "2024-09-30 14:45:12"

vaqt = datetime.strptime(sana, "%Y-%m-%d %H:%M:%S")

new = vaqt + timedelta(days=7, hours=3, minutes=15)

result = new.strftime("%A  %d-%B-%Y %H:%M:%S")

print(result)
