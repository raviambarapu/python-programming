try:
    year=int(input("Enter any year: "))
    if(year>0):
        if(year%400==0):
            print(year,"is an leap year.")
        elif(year%4==0):
            print(year,"is an leap year.")
        elif(year%100==0):
            print(year,"is not an leap year.")
        else:
            print(year,"is not an leap year.")
    else:
        print("Enter valid year")
    n=year%4
    print("Pre Year:",year-n)
except ValueError:
    print("Enter valid year")
