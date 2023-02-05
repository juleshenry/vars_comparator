#Vars Comparator#

When unit tests disappear, do not fear! There is a way to grock refactors for untested integration Python code.

What's the major issue with refactoring code with no unit tests? (Hint: don't say lack of unit tests). There is not a way to guarantee the refactor performs the same function as the original.

In the case where many one-off scripts are used, this script should allow comparison of the outcome of the original and refactored by inspecting the outcome variable space.

Example One:

A.py 
>> x = 5

B.py
>> y = 5

We have A ~= B, so we can say the refactor is equivalent.



