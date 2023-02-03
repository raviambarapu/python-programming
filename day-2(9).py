month=input("Enter the month:")
date=int(input("Enter the date:"))
if(month=="Mar" and date>=20) or (month=="Apr")or (month=="May")or(month=="Jun" and date<21 ):
    print("Summer Season")
elif(month=="Jun" and date>=21)or(month=="Jul")or(month=="Aug")or (month=="Sep" and date<22):
    print("spring season")
elif(month=="Sep" and date>=22 )or (month=="Oct") or (month=="Nov")or(month=="Dec" and date<21):
    print("Fall season")
elif(month=="Dec" and date>=21) or(month=="Jan") or(month=="Feb")or (month=="Mar" and date<20):
    print("Winter season")
