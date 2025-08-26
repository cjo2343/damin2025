import drunken_1
import drunken_2

# Create a list of 5 drunken people
#drunks = drunken_1.create_drunken(5)
#print(f"Starting positions: {drunks}")

# Run the simulation for 100 steps
#for i in range(100):
 #   drunks = drunken_1.step(drunks)  # <-- Add the prefix here
  #  print(f"Step {i+1}: {drunks}") 


#remember that the create_drunken creates n unique drunken people, so each number in the array represents one person
#And each person starts from 0
#Each array line shows each persons steps, so for the first person at index 0, 
#we see that he starts at 0, and then for each new print of the array, we can follow his steps from the very first to the last one (at 100 steps)

#We know that the expected distance each person will "travel" is the square root of n, 
# which gives us the square root of 100 = 10. When we look at the positions for each person, 
# we see that the postions hover just around 10 for most of the time, which is quite interesting. 
# I will, tomorrow, try to calculate the Average distance for one person to see if it is proportional to 10.

# dr = dr + single_step(move), for each step, it saves the value of that position as dr. 
# So for the first person at step number 3, we have dr = 0 and then we can see that the variable move = 0 since we go to position -1, 
# so we get dr = 0 + single_step(0) = -1+-1 = 2


# Part 2

drunk2 = drunken_2.create_drunken(10)
#print(drunk2)
moved_drunken = drunken_2.random_walk(drunk2,10)
#print(moved_drunken)
bins = 10 # number of bins
visual = drunken_2.plot_drunken(moved_drunken, bins)

# I have decided to use a much smaller number than 1000 to better see waht the plot actually shows. 
# It shows 