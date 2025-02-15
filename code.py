#1. Given a sorted array of positive and negative numbers. 
arr = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
squared_arr = []  
for num in arr:  
    squared_arr.append(num * num)  
squared_arr.sort()  
print(squared_arr)  
#Output: [4, 16, 25, 25, 49, 121, 144, 225]

#2 Design an immutable class with following attributes
class Employee:
    def __init__(self, name, emp_id, date_of_joining, addresses):
        self._name = name
        self._emp_id = emp_id
        self._date_of_joining = date_of_joining
        self._addresses = tuple(addresses)  

    @property
    def name(self):
        return self._name

    @property
    def emp_id(self):
        return self._emp_id

    @property
    def date_of_joining(self):
        return self._date_of_joining

    @property
    def addresses(self):
        return self._addresses  

    def __repr__(self):
        return (
            f"Employee(name='{self.name}', emp_id='{self.emp_id}', "
            f"date_of_joining='{self.date_of_joining}', addresses={self.addresses})"
        )


class Address:
    def __init__(self, street, city, zip_code):
        self._street = street
        self._city = city
        self._zip_code = zip_code

    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city

    @property
    def zip_code(self):
        return self._zip_code

    def __repr__(self):
        return f"Address(street='{self.street}', city='{self.city}', zip_code='{self.zip_code}')"



address1 = Address("123 Main St", "Nagpur", "12345")
address2 = Address("456 Elm St", "Pune", "67890")

employee = Employee("John Doe", "E123", "2023-05-01", [address1, address2])

print(employee)
print(employee.addresses)  

#3 array of Red Green Blue balls...
def sortBalls(arr):
    return ['B'] * arr.count('B') + ['G'] * arr.count('G') + ['R'] * arr.count('R')

arr = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
print(sortBalls(arr))  # Output: ['B', 'B', 'B', 'G', 'G', 'G', 'G', 'R', 'R'] 

#4  arrival and departure times of trains..
def min_platforms(arr, dep):
    arr.sort()
    dep.sort()
    
    i, j = 0, 0  # Pointers for arrival and departure
    platform_needed = 0
    max_platforms = 0
    
    while i < len(arr):
        if arr[i] < dep[j]:  # Train arrives before the previous one departs
            platform_needed += 1
            max_platforms = max(max_platforms, platform_needed)
            i += 1
        else:  # Train departs
            platform_needed -= 1
            j += 1
    
    return max_platforms

arr1 = [900, 940, 950, 1100, 1500, 1800]  # 9:00, 9:40, ...
dep1 = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platforms(arr1, dep1))  # Output: 3

arr2 = [900, 940]
dep2 = [910, 1200]
print(min_platforms(arr2, dep2))  # Output: 1

#5  Sort hashmap by value.
def sort_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

employees = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
print(sort_by_value(employees))  
# Output: {102: 'Jane Smith', 101: 'John Doe', 103: 'Peter Johnson'}