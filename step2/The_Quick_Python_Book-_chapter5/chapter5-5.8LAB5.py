'''In this lab, the task is to read a set of temperature
data (the monthly high temperatures at Heathrow Airport for 1948 through
2016) from a file and then find some basic information: the highest and low-
est temperatures, the mean (average) temperature, and the median tempera-
ture (the temperature in the middle if all the temperatures are sorted).
The temperature data is in the file lab_05.txt in the source code directory for
this chapter. Because I haven’t yet discussed reading files, here’s the code to
read the files into a list:'''
'''Determine how many unique temperatures are in the list.'''

temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))
print(temperatures)
maximum = max(temperatures)
minimum = min(temperatures)
avg = sum(temperatures)/len(temperatures)
temperatures.sort()
if len(temperatures)%2:
    median = temperatures[int(len(temperatures)/2)]
else:
    median = 0.5 * (temperatures[int(len(temperatures)/2)] + temperatures[int(len(temperatures)/2)-1])

unique_temperatures = list()
for i in temperatures:
    if temperatures.count(i) == 1:
        unique_temperatures.append(i)
print(len(unique_temperatures))