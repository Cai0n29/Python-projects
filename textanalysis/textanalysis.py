def count(filepath, word_list):
    """

    Parameters
    ----------
    filepath : 
    path of the file
    
    word_list : str
    counting the specified list of words

    Returns
    -------

    """
    
    #Opening the text file
    with open(filepath) as file:
        text = file.read()
    n =0
    for word in text.split():
        if word.lower() in word_list:
            n+=1
    return n