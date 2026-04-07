import numpy as np
#data provided by Gemini  

# Day names
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Daily high temperatures in Celsius
temps_c = np.array([22.5, 24.8, 21.0, 19.5, 25.2, 28.1, 26.5])

#challenge 1: Create a new array where temps are converted to farenheit
temps_f = (temps_c*1.8)+32

#challenge 2: find the mean, min, and maximum of the temps for the week 
temps_mean_c = np.mean(temps_c)
temps_max_c = np.max(temps_c)
temps_min_c = np.min(temps_max_c)


#Create a boolean mask to find all the days where the temp is >23
bool_mask = temps_c > 23
print(temps_c[bool_mask])

#Slicing: Extract the temperatures for the "Weekend" (the last two elements of the array).
print(temps_c[-3:-1])

#Searching the index of the hottest day 
hottest_ind = np.argmax(temps_c)
print (days[hottest_ind] +" records the hottest temp in the week.")