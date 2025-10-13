# age : int
# name: str
# height: float
# is_human: bool

def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
police_check(19)

def greeting(name: str) -> str:
    return "Hello "+ name

#  This is Know as TYPE HINT in PYTHON.