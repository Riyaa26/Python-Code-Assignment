def are_anagrams(str1, str2):
    str1_clean = str1.replace(" ", "").lower()
    str2_clean = str2.replace(" ", "").lower()
    return sorted(str1_clean) == sorted(str2_clean)

string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)

if result:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
