while True:
    num=int(input("Enter a number:-"))
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
    ans=input("Do you want to continue(y/n):-")   
    ans=ans.lower() 
    if ans!='y':
        break
        
        