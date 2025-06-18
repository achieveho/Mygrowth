import datetime

def get_birth(age):
    if (0 < age <= 120):
        year = datetime.datetime.now().year
        return year - (age + 1)
    return

print(get_birth(24))