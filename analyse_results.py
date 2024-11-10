import numpy as np
import matplotlib.pyplot as plt

class Point:
    import numpy
    primes = [2,3,5,7]
    def __init__(self, code: str, freq: int):
        self.code = code
        self.freq = freq
        self.dig_list = self.get_dig_list()
        self.stdev = np.std(self.dig_list)
        self.mean = np.mean(self.dig_list)
        self.non_zero = 4-self.dig_list.count(0)
        self.primes = self.count_primes()


    def get_dig_list(self):
        dig_list = []
        for digit in self.code:
            dig_list.append(int(digit))
        return dig_list
    
    def count_primes(self):
        prime_count = 0
        for digit in self.primes:
            prime_count += self.dig_list.count(digit)
        return prime_count

    def __str__(self):
        return f"Code: {self.code}\n Freq: {self.freq}\n Std.Dev: {self.stdev}\n Mean: {self.mean}\n Non-Zero: {self.non_zero}\n Primes: {self.primes}\n"



with open ("Results.csv") as new_file:
    points = []
    for line in new_file:
        parts = line.split(';')
        points.append(Point(parts[0],int(parts[1])))

def write_to_dic(pointlist: list, attribute: str):
    #creates a dictionary that adds up all the frequencies for a specific value
    new_dic = {}

    for point in pointlist:
        key = getattr(point,attribute)
        if key not in new_dic:
            new_dic[key] = [0,0,0]
        #first entry in list is the total frequency, secodn entry is the number of points counted
        if point.freq > 0:
            new_dic[key][0] += 1
        new_dic[key][1] += 1

    for key in new_dic:
        new_dic[key][2] = new_dic[key][0]/new_dic[key][1]
        #new_dic[key] = new_dic[key][2]
    return new_dic


def find_by_attr(pointlist:list, attribute_name: str, attribute_val):
    #returns the list of points matching that attribute
    match_list = []
    for point in pointlist:
        checkval = getattr(point, attribute_name)
        if checkval == attribute_val:
            match_list.append(point)
    return match_list

def dic_sum(mydictionary: dict):
    runsum = 0
    for key in mydictionary:
        runsum += mydictionary[key][0]
    return runsum

mean_dic = write_to_dic(points, 'non_zero')

#plt.figure()
yval = [mean_dic[key][2] for key in mean_dic]
yfreq = [mean_dic[key][1] for key in mean_dic]
xval = [key for key in mean_dic]


"""
fig, ax1 = plt.subplots()

# Plot percentages on the primary y-axis
ax1.plot(xval, yval, color='b', label='Percentage', linestyle = "", marker = 'x')
ax1.set_xlabel('X-axis Label')            # Label for the x-axis
ax1.set_ylabel('Percentage', color='b')   # Label for the left y-axis
ax1.tick_params(axis='y', labelcolor='b') # Color the y-axis ticks

# Create a second y-axis sharing the same x-axis
ax2 = ax1.twinx()
ax2.plot(xval, yfreq, color='r', label='Frequency')
ax2.set_ylabel('Frequency', color='r')    # Label for the right y-axis
ax2.tick_params(axis='y', labelcolor='r') # Color the y-axis ticks

# Optionally add legends for clarity
fig.tight_layout()  # Adjust layout to prevent overlap
plt.show()
"""
print(f"{dic_sum(mean_dic)} out of 10,000 cannot make 10")


"""




mean_data = write_to_dic(x_mean,y_freq)

for item in mean_data:
    print(f"{item}: {mean_data[item]}")

x_stdev = np.array([item.stdev for item in points])
x_non_zero = np.array([item.non_zero for item in points])
x_primes = np.array([item.primes for item in points])

plt.figure()
plt.scatter(x_stdev[:],y_freq[:],marker ='.',s =0.5)
plt.xlim(xmin=0, xmax = 10)
plt.xlabel("Std Deviation of Digits")
plt.ylabel("Frequency")
plt.title("Frequency vs Std Dev of Digits")


plt.figure()
plt.scatter(x_non_zero[:],y_freq[:],marker ='.',s =0.5)
plt.xlim(xmin=0, xmax = 5)
plt.xlabel("Qty of Non-Zero Digits")
plt.ylabel("Frequency")
plt.title("Frequency vs Non-Zero Digits")
plt.show()


plt.figure()
plt.scatter(x_primes[:],y_freq[:],marker ='.',s =0.5)
plt.xlim(xmin=0, xmax = 5)
plt.xlabel("Qty of Prime Digits")
plt.ylabel("Frequency")
plt.title("Frequency vs Qty of Primes")
plt.show()




figure2 = plt.scatter(x_stdev[1234:1244], y_freq[1234:1244])
plt.show()

"""