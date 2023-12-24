def calculator(midterm, final, passG):
    result = (midterm*(2/5)) + (final*(3/5))
    if(result >= passG):
        print(f"Congratulations, You have successfully passed the lesson!\nYour average:{result}")
    
    elif(0 <= result < passG):
        resit = int(input(f"You failed the lesson.\nYour average:{result}\nYour resit result: "))
        result = (midterm*(2/5)) + (resit*(3/5))

        if(result >= passG):
            print(f"Congratulations, You have successfully passed the lesson!\nYour average:{result}")

        elif(0 <= result < passG):
            print(f"You failed the lesson.\nYour average:{result}") 

        else:
            print("İncorrect information entry, try again.")
    
    else:
        print("İncorrect information entry, try again.")

passG = int(input("Your pass grade:"))
midterm = int(input("Your midterm result:"))
final = int(input("Your final result:"))
calculator(midterm, final, passG)