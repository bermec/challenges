import re
from collections import Counter

words = re.findall(r'\w+', open('holmes.txt').read().lower())
print(Counter(words).most_common(10))