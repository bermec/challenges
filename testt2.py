

S = input("String: ")
is_limit = lambda min, max: len(set(S[min:max + 1])) > 2
max_substr = ""
for i in range(len(S)):
    cur_str = "".join([S[j] for j in range(i, len(S)) if not is_limit(i, j)])
    max_substr = cur_str if (len(cur_str) >= len(max_substr)) else max_substr
print(max_substr)