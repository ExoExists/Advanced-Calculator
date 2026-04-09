import math

userInput=input("Enter your calculation: ")

def calculator(userInput):
    calculation = userInput.split()
    listLength=len(calculation)
    total=int(calculation[0])
    
    #print("List Length: " + str(listLength))
    bedmass=False
    bedmasNumber=False

    for index,currentItem in enumerate(calculation):
        #print("Index: "+ str(index))
        #print("Current Item: " + currentItem)
        if index>0:
            previousItem=calculation[index-1]
          #  print("Previous Item: " + previousItem)
        if index<=listLength-2:
            nextItem=calculation[index+1]          
         #   print("Next Item: " + nextItem)
        if currentItem=="*":
            total=currentItem*int(nextItem)
        if currentItem=="/":
            total=currentItem/int(nextItem)

    for index,currentItem in enumerate(calculation):
        #print("Index: "+ str(index))
        #print("Current Item: " + currentItem)
        if index>0:
            previousItem=calculation[index-1]
          #  print("Previous Item: " + previousItem)
        if index<=listLength-2:
            nextItem=calculation[index+1]          
         #   print("Next Item: " + nextItem)
        if currentItem=="+":
            total=total+int(nextItem)
        if currentItem=="-":
            total=total-int(nextItem)
    #        if currentItem=="*":
     #           total=total*int(nextItem)
      #      if currentItem=="/":
       #         total=total/int(nextItem)
    print(total)
calculator(userInput)

