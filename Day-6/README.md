This algorithm takes me a little bit to think over the logic of but it's a pretty simple way to solve.  Taken the fact that no elements can be repeated, i used a dictionary to s store the differnce between the target and current element with the location of the num stored m as the value.



here is an example of it.

input array [2, 7, 11, 15]

dictionary {}

target 9

we enumerate over the input array. We check to see if the current number is in the dictionary. it isnt, so then we add the target - num and store that as the key with the value being the position of num.  

dictionary {7:0}

now we iterate through to the next item in the array and we look to see if the num, 7, is in the dictionary and it is.  adding 2 + 7 equals the target. so now since we met our match, we return the value of the num in the dict which is the value of the first number and the location of the current number

so we return [0,1]
