favourite_languages = {'Sarah': 'python',
                       'Jane': 'C',
                       'Phil': 'Ruby',
                       'Sam': 'Python'}
print(favourite_languages)

for name in favourite_languages:
    print(name.title())
friends = ['Phil', 'Sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +

              favourite_languages[name].title() + "!")
