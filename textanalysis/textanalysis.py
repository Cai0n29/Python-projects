def count(filepath, word_list):
    #Opening the text file
    with open(filepath) as file:
        text = file.read()
    n =0
    for word in text.split():
        if word.lower() in word_list:
            n+=1
    return n