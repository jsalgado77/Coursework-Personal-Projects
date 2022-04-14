def arithmetic_arranger(problems, show = False):
  problemFormatted = []

  for index, value  in enumerate(problems):

    operation = value.split(" ")

    if len(problems) > 5:
      return "Error: Too many problems."

    if operation[1] not in '+-':
      return "Error: Operator must be '+' or '-'."

    try:
      value1 = int(operation[0])
      value2 = int(operation[2])

    except ValueError:
        return "Error: Numbers must only contain digits."
      

    if len(operation[0]) > 4 or len(operation[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
      

    
    largestInt = max(operation[0],operation[2])

    width = len(largestInt) + 2

     # format and put together the lines that will printed out

    line1 = f"{operation[0] :>{width}}"


    line2 = operation[1] + f"{operation[2]:>{width-1}}"

    d = '-' * width
      
    if operation[1] == '+':
      answer = str(int(operation[0]) + int(operation[2]))

    if operation[1] == '-':
      answer = str(int(operation[0]) - int(operation[2]))

    fa = f"{answer:>{width}}"

        # append formatted lines into an array

    try:
      problemFormatted[0] += (' ' * 4) + line1
    except IndexError:
      problemFormatted.append(line1)

    try:
      problemFormatted[1] += (' ' * 4) + line2
    except IndexError:
      problemFormatted.append(line2)

    try:
       problemFormatted[2] += (' ' * 4) + d
    except IndexError:
      problemFormatted.append(d)  


    if show:
        
      try:
        problemFormatted[3] += (' ' * 4) + fa
      except IndexError:
        problemFormatted.append(fa)
                
                
    
    arranged_problems = f"{problemFormatted[0]}\n{problemFormatted[1]}\n{problemFormatted[2]}"
    
    if show:
      arranged_problems = arranged_problems + f"\n{problemFormatted[3]}"
   


  return arranged_problems