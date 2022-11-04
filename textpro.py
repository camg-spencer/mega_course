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
    