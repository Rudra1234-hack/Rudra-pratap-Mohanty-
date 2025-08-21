#what is dictionary in python
'''
    A dictionary in Python is a built-in data type that allows you to store and manage data in
    key-value pairs. Each key in a dictionary is unique, and it maps to a specific value. This structure is useful for quickly accessing data based on a unique identifier (the key).
    Dictionaries are mutable, meaning you can change their content after creation, and they are unordered collections
    of items, meaning the order of items is not guaranteed.
    Dictionaries are defined using curly braces `{}` with key-value pairs separated by colons `:`.
    Example:
    ```python   
    my_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }
'''
# Example of a dictionary in Python
my_dict = { 
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}   
# Accessing values in a dictionary
print(my_dict['name'])  # Output: Alice
# Adding a new key-value pair
my_dict['job'] = 'Engineer'
# Modifying an existing value
    
# removing a key-value pair
my_dict.pop('age')
#deleting a key-value pair
del my_dict['city']
#keys in a dictionary
print("Keys in the dictionary:", my_dict.keys())
#items in a dictionary
print("Items in the dictionary:", my_dict.items())

#getting the value of a key
print("Value of 'name':", my_dict.get('name'))

#pop method
print("Popped value of 'job':", my_dict.pop('job', 'Key not found'))

#clear method
my_dict.clear()
print("Dictionary after clearing:", my_dict)

#popitem method
my_dict = {
    'name': 'Alice',    
    'age': 30,
    'city': 'New York'
}
print("Popped item:", my_dict.popitem())  # Removes and returns the last inserted key-value pair

#copy method
my_dict_copy = my_dict.copy()
print("Copied dictionary:", my_dict_copy)   

#update method
my_dict.update({'country': 'USA', 'job': 'Engineer'})
print("Updated dictionary:", my_dict)

