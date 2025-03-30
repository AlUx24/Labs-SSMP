languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "Ruby": "Yukihiro Matsumoto"
}

for lang, creator in languages.items():
    print(f"My favorite programming language is {lang}. It was created by {creator}.")

languages["JavaScript"] = "Brendan Eich"
languages["C#"] = "Anders Hejlsberg"

del languages["Ruby"]

print("\nОновлений словник:")
for lang, creator in languages.items():
    print(f"{lang}: {creator}")
