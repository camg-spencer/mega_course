# build list of inputs
# put correct punctuation 
# capitalize first letter & space between sentences
# end when \end is entered
# input prompt says "Say something: "

def sentence_maker(phrase):
    q_words = ("how", "what", "why", "who", "when", "where")
    cap = phrase.capitalize()
    
    if phrase.startswith(q_words):
        return f"{cap}?"
    else:
        return f"{cap}."
    
phrases = []
    
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        phrase = sentence_maker(user_input)
        phrases.append(phrase)

solution = " ".join(phrases)
print(solution)