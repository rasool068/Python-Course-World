'''
fa = eval(input("Follows Account: "))
if fa:
    cf = eval(input("Close Friend: "))
    if cf:
        print("Visible story")
else:
    print("Follow the account")

reg = eval(input("Registered: "))
if reg:
    fee = (input("Fees paid: "))
    if fee:
        print("Tournament entry confirmed")
    else:
        print("Fees not paid")
else:
    print("SIGN UP FIRST")
'''
data = {
    'kohli':{'match':True,'score':99,'score2':100,'score3':80}
    'rohit':{'match':True,'score':80,'score':90,'score3':85}
    'hardik':{'match':True,'score':30,'score2':40,'score3':55}
    'bumrah':{'match':False,'score':None,'score2':None,'score3':None}
    'dhone':{'match':True,'score':33,'score2':10,'score3':0}
}
name = input("Enter the name: ")
if name in data:
    if data[name]['match']
    sum = data[name]['score'] + data[name]['score2'] + data[name]['score3']
    print(f"Hello {name}!!!")
    print(f"Your average score is {avg}")
    if avg >= 90:
        print("Best Batsman")
    elif avg >= 80:
        print("Good Batsman")
    elif avg >= 70:
        print("Batsman , work hard ")
    elif avg >= 30:
        print("on hold")
    else:
        print("not selected")
else:
    print(f'{name}not found')
    