def find_word(message):

    words = message[:-1].split(" ")
    msg_matrix=[ [0 for i in range(0,len(words))] for j in range(0,len(words))]

    for i in range(0, len(words)):
        for j in range(0, len(words)):
            if words[i] != words[j]:
                msg_matrix[i][j] = compute_likeness(words[i].lower(), words[j].lower())
    print_matrix(words, msg_matrix)
    col = [ [msg_matrix[i][j]  for j in range(0,len(words)) if msg_matrix[i][j] != 0] for i in range(0, len(words))]
    avgs = [round(float(sum(c))/len(c),3) for c in col]
    print avgs
    w =  words[avgs.index(max(avgs))].lower()
    print w
    return w

def print_matrix(words, matrix):
    for i in range(0, len(words)):
        row = words[i] + ":"
        for j in range(0, len(words)):
            row += str(matrix[i][j]) + " "
        print row

def compute_likeness(w1, w2):
    likeness = 0

    # rule 1: must begin and end with the same letter, regardless of case
    if w1[-1:] == w2[-1:]:
        likeness += 10

    if w1[1] == w2[1]:
        likeness += 10

    # rule 2: compare the lenghts
    if len(w1) <= len(w2):
        likeness += (float(len(w1))/len(w2)) * 30
    else:
        likeness += (float(len(w2))/len(w1)) * 30

    # rule 3: determine the common to unique letters ratio
    unique_letters = len(set(w1+w2))
    common_letters = len(set(w1).intersection(set(w2)))

    likeness += (float(common_letters)/unique_letters) * 50

    return round(likeness,3)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Friend Fred and friend Ted.") == "friend", "Control"
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
"""    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
"""
