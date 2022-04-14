def add_time(start, duration, optional = None):
      
      newHr = 0
      
      newMin = 0

      daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

      

      timeAbb = start.split(" ")

      hrMin = timeAbb[0].split(":")

      timeAdd = duration.split(":")

      if (timeAbb[1] == "PM"):
            newHr = (int(hrMin[0])+12) + int(timeAdd[0])

            newMin = int(hrMin[1]) + int(timeAdd[1])

      elif (timeAbb[1] == "AM"):
            
            if (hrMin[0] == "12"):
                  hrMin[0] = "0"

            newHr = int(hrMin[0]) + int(timeAdd[0])
            
            newMin = int(hrMin[1]) + int(timeAdd[1])

            
      if (newMin >= 60):

            newHr += 1

            newMin = newMin%60

      fullDays = newHr//24


      newHr = newHr%24

      if (newHr == 0):
            timeAbb[1] = "AM"
            newHr = 12


      elif (newHr > 12):
            timeAbb[1] = "PM"
            newHr -= 12

      elif (newHr == 12):
            timeAbb[1] = "PM"
            
      else:
            timeAbb[1] = "AM"
            

                  
      new_time = f"{newHr:01}" + ":" + f"{newMin:02}" + " " + timeAbb[1]

      if (fullDays == 1):
            new_time = new_time + " (next day)"

      if (fullDays >1):
            new_time = new_time + " (" + str(fullDays) + " days later)"


      if (optional != None):


            for index, value in enumerate(daysOfWeek):

                  if (value.lower() == optional.lower()):

                        if ((index + fullDays)<= 6):

                              newOptional = index + fullDays

                              
                        if ((index + fullDays) > 6):

                              newOptional = (index + fullDays)%7

                        
                  
            if (fullDays == 0):       
                  new_time = f"{newHr:01}" + ":" + f"{newMin:02}" + " " + timeAbb[1] + ", " + daysOfWeek[newOptional]

            if (fullDays == 1):
                  new_time = f"{newHr:01}" + ":" + f"{newMin:02}" + " " + timeAbb[1] + ", " + daysOfWeek[newOptional] +  " (next day)"

            if (fullDays >1):
                  new_time = f"{newHr:01}" + ":" + f"{newMin:02}" + " " + timeAbb[1] + ", " + daysOfWeek[newOptional] + " (" + str(fullDays) + " days later)"
                        

      return new_time
      



def main():

      print(add_time("11:01 PM", "125:44", "Tuesday"))



main()

