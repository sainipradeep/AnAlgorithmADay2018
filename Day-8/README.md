The main points behind this algorithm is that we are only evaluating a string with valid parentheses.  anything else will cause as error and will be returned as false.  so small changes can be made to allow for non parentheses to be "skimmed" over but in this case, anything that is not defined in the valueKeyDict, will error.  

So the logic behind this is to create a stack, and a dict that defines the key and values.I set the key to be the closing parentheses and the value as the opening of the perentheses.

 So i interate through the  string and first check to see if it's in the dict values.  if it is then it's an opening parenthese and i just append to the stack.  if it isnt then i check if its in the dict's keys meaning it is a closing bracket. so i check if the stack is empty. if it's empty then it does not have a matching opening bracket and it will error.  if not then i check if the value for the item in the dict is equal to the last item attned to the stack.  if it isn't then i know the opening and closing brackets are NOT matching and i return false.

now i have my final else statement.  this is to catch anything not defined in the dictionary.  i return false in this statement

now my final return is stack == [].  it should be cleared out and empty at this point. is there is anything leftover then a false is returned.


