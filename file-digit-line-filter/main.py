# Write a program that reads a file line by line and prints only those lines that contain a number.

with open(".txt", "r") as f:
        line_no = 1
        lis = ["0","1","2","3","4","5","6","7","8","9"]
        found = False
        
        while True:
            data = f.readline() # read linebyline
            if data == "": #if data got empty
                   break #break
         
            for i in lis:                                                      #loop through list
                  if i in data:                                               #check each number in data 
                        print(f"Line content: {data}",end="")                #if found, print that line
                        print(f"Line number: {line_no}", end="\n")                         # and line number 
                        found = True                                            # and chang the  found state
                        break  #prevents duplication if line numer got matched with number on the line
            line_no += 1                                                      #if not found in the first line, increase line no count.
  
        if found == False:                                                   # if found stays false, means we didnt find it in loop. 
              print("A line with an int doesnt exist.")                        # so print that