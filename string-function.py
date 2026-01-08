
# string concatination
print("string concatination" + " hello" + " world")

a="govind"
print("Output of String function:", a.upper())
print("Output of String Len:", len(a))
print("Access Charactor from String:", a[0])
print("Slicing Charactors from String:", a[0:4])
print("Slicing start to 4 Charactors from String:", a[:4])
print("Slicing 4 to end of the string Charactors from String:", a[4:])
print("Slicing minus string Charactors from String:", a[-4:-1])

# Following are the string functions inm python

# s.find(sub) : Returns the lowest index of the substring sub found in the string. Returns -1 if not found.
# s.index(sub) : Same as find(), but raises a ValueError if the substring is not found.
# s.replace(old, new) : Returns a new string with all occurrences of old substring replaced by new substring.
# s.count(sub) : Returns the number of non-overlapping occurrences of the substring sub.
# s.startswith(prefix) : Returns True if the string starts with the specified prefix.
# s.endswith(suffix) : Returns True if the string ends with the specified suffix.

# s.upper() : Converts all characters in the string to uppercase.
# s.lower() : Converts all characters in the string to lowercase.
# s.capitalize() : Returns a string with only the first character capitalized and the rest lowercase.
# s.title() : Converts the first character of each word to uppercase.
# s.strip() : Removes leading and trailing whitespace (or specified characters).
# s.lstrip() : Removes leading (left) whitespace/characters.
# s.rstrip() : Removes trailing (right) whitespace/characters.

# s.split(sep) : Splits the string into a list of substrings based on the specified separator (sep).
# s.partition(sep) : Splits the string into a tuple of three parts: (before separator, separator, after separator).
# sep.join(iterable) : Joins the elements of an iterable (like a list) into a single string, using sep as the separator.

# s.isalpha() : Checks if all characters are alphabetic (A-Z, a-z) and the string is not empty.
# s.isdigit() : Checks if all characters are digits (0-9) and the string is not empty.
# s.isalnum() : Checks if all characters are alphanumeric (letters or numbers) and the string is not empty.
# s.isspace() : Checks if all characters are whitespace and the string is not empty.
# s.islower() : Checks if all cased characters are lowercase.
# s.isupper() : Checks if all cased characters are uppercase.
