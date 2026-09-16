"""
Exercise 2: Explain and fix a bug with Copilot Chat

The function below is real, runnable code. It computes the average of
a list of numbers, but it has a bug.

1. Select the `average` function, including the def line.
2. Open Copilot Chat and ask it to explain what the function does.
3. Run this file. Watch the second call crash.
4. Ask Copilot Chat why the crash happens, then ask it to fix the
   function. Read the fix before you accept it. Does it handle an
   empty list the way you would want it to?
"""


def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


print(average([1, 2, 3, 4, 5]))
print(average([]))  # This line raises ZeroDivisionError.
