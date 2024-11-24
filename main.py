from greet import greetings
from translate import Translator

# make the translator object
# to translate in Portuguese
translator = Translator(to_lang='pt')

for g in greetings:
    print(translator.translate(g))  # To translate g
