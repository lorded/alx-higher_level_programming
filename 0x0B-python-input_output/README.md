TASkS
Certainly! Here are the descriptions for each task:
Task 0: Read File

Write a function read_file that reads a text file (UTF8) and prints its content to stdout. The function should use the with statement and not manage file permission or file doesn't exist exceptions.
Task 1: Write to a File

Write a function write_file that writes a string to a text file (UTF8) and returns the number of characters written. The function should use the with statement, create the file if it doesn't exist, and overwrite the content if it already exists.
Task 2: Append to a File

Write a function append_write that appends a string at the end of a text file (UTF8) and returns the number of characters added. If the file doesn't exist, it should be created. Use the with statement.
Task 3: To JSON String

Write a function to_json_string that returns the JSON representation of an object (string). Don't manage exceptions if the object can't be serialized.
Task 4: From JSON String to Object

Write a function from_json_string that returns an object (Python data structure) represented by a JSON string. Don't manage exceptions if the JSON string doesn't represent an object.
Task 5: Save Object to a File

Write a function save_to_json_file that writes an object to a text file using a JSON representation. Use the with statement, and don't manage exceptions if the object can't be serialized.
Task 6: Create Object from a JSON File

Write a function load_from_json_file that creates an object from a JSON file. Use the with statement, and don't manage file permissions/exceptions.
