# In this program we'll create a pattern and see what strings match the pattern.
# The pattern will be a sentence pattern.
#
# How [adverb] ... !
#
# Thus the sentence "How lovely the sky is!" matches the pattern.
# The sentence "How quickly he ran!" also matches the pattern.

import re

# The re.compile method gives us a pattern object. The pattern object has a method called match
pattern = re.compile(r'How [a-zA-Z]+ly .*!')

strings = [
    "How lovely the sky is!", 
    "How quickly he ran!", 
    "How lovely the day is!",
    "How happily she sings!",
    "How beautifully she knits!",
    "The class convenes on Friday",
    "The school starts in autumn",
    "The seminar begins today",
    "How hot it is today",
    "How cold it was yesterday",
    "How loudly he sings",
    "How softly he sings!"]

print("Matches:")
for s in strings:
    if pattern.match(s):
        print(s)
