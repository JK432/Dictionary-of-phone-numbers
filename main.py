# Write a Python program to create a dictionary of phone numbers and names of five persons. Display the cointents of the dictionary in alphabetical order of names 
ph={}
i=0
while(i<5):
  key = input() 
  value = input() 
  ph[key] = value
  i=i+1


 
sorted_keys = ph.items()
new_values = sorted(sorted_keys)
print(new_values)