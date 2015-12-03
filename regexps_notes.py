#!/usr/bin/env python3
__author__ = "hero24"
# This is only an example of how to use built-in Python regular expression module!
# Regexp example:
import re 
# import re module (Regular Expressions)

# Understanding expressions:
# before you continue take a minute to understand the format of regular expressions
# Quick reference:
#  -"\w" Word character - any alphanumeric + _
#  -"\W" Nonword character - any non-alphanumeric except _
#  -"\d" Digit
#  -"\D" Nondigit
#  -"\s" Whitespace (\t,\n,\r,\f,\v)
#  -"\S" Nonwhitespace (\t,\n,\r,\f,\v)
#  - * - match 0 or more elements
#  - + - match 1 or more elements
#  - ? - match 0 or 1 elements
#  - | - or
#  - ^ - not
#  - "string" - any string matches it self
#  -"[A-Z]" - range from A to Z
#  -"[A-Za-z0-9]" - range from A to Z then from a-z then 0-9
#

example_string = "Linux is only free if your time has no value. ~ Jamie Zawinski ~ 123"

# Regular Expressions, can be used 2 ways
# - as a compiled expression
# - as parameter in function

# Using complied expressions:
# Compiled expression is an object:
# re.compile(expression,flags=0)
expression_object = re.compile('(?P<vowels>a|o|i|e|u|y).+(?P<numbers>\d)')
# matches a or o or i or e or u or y followed by some characters followed by a number
# (?P<group_name>regular_expression) - defining a match group with 'group_name' as name

match_object = expression_object.search(example_string)
# .match and .search return match objects
# note .match, looks for match only at the start of the string
# where as .search looks through entire string.
# both will return only first match.
print("===>Entire match :", match_object.group())
# Grouping:
# matches in expression can be named and grouped accordingly to their names, or index values
print("===>Match of \d (number)", match_object.group(2))
# accessing by indexes: 0 -> entire match
# 1+ are groups, that have been defined.
print("===>Match of vowels :", match_object.group('vowels'))
# accessing by pre-defined names

# Getting all matches of expression:
expression_object = re.compile('(?P<vowels>a|o|i|e|u|y)')
match_object = expression_object.findall(example_string)
# returns a list of all matched elements
print("===>All matches of vowels :", match_object)

# Substituting (replacing) matches with a string
example_string = expression_object.sub("<this was matched by regex>", example_string)
# substitutes every match with '<this was matched by regex>'
print("===>Substituting every match by <this was matched by regex> :", example_string)

# Split the item when pattern matched
splitted_string = expression_object.split(example_string)
# return a list of strings splitted at the point of match
print("===>Split string :", splitted_string)

# Iterate over matches
iterated_matches = expression_object.finditer(example_string)
# creates iterable object, that 'yield's any match that is found just like range(x)
# 'yield's numbers in range x
for i in iterated_matches:
    print("==> iterated match:", i.group())

# Using functions instead of objects:
example_string = "Any string that contains characters and a valid hex color code like #F0FAFF"
matched_string = re.search("#([a-fA-F0-9]){3}(([a-fA-F0-9]){3})", example_string)
# re.search(regular_expression,string_to_match,flags=0)
# above search will match a hex color code.
print("==> Found string :", matched_string.group())
example_string = re.sub("(\w+)", r'<p>\1</p>\n', example_string)
# Match any 'word' and put it into <p> tags. (Substitute a matched word for <p>matched word</p>\n))
print("===> Substituted string :",example_string)
example_string = re.escape(example_string)
# Backslashes (escapes) any non alphanumerical characters
print("===> Escaped string :",example_string)
example_list = re.findall("\w*in\w*",example_string)
# returns all matches of \w*in\w* (does it contain word in, or any word that contains 'in'
print("===> List of matches :",example_list)
example_list[0] = re.split("i",example_list[0])
# splits example_list[0] (word string) with match as delimiter (in this case letter i) into list
print("===> Split list :",example_list[0])
example_list[1] = re.finditer("\w",example_list[1])
# creates iterable object, that 'yield's any match that is found just like range(x)
# 'yield's numbers in range x
# matches any alphanumeric character
for i in example_list[1]:
    print(i.group())

# Notes to take into account:
# .group is required to print out, or access string matched by match, search or example_list
# as those functions create a match object, on successful match! You should always test if your
# match exists before calling group on your variable, because if match or search does not match
# any pattern it returns None, and noneType has no method called group.
# This can be done using simple if statement:

# color = "#FFFFFF"
color = ""
example_string = "Any string that contains characters and a valid hex color code like %s" % color
matched_string = re.search("#([a-fA-F0-9]){3}(([a-fA-F0-9]){3})", example_string)
if matched_string:
    print("===>",matched_string.group())
else:
    print("No positive match: ",matched_string)
