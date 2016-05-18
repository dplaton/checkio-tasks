def longest_palindromic(text):
    if len(text) == 1:
        return text

    longest = ""
    for idx in range(0,len(text)-1):
        string = text[idx:]
        for i, e in enumerate(string,1):
            if string[:i] == string[i-1::-1]:
                longest = string[:i] if len(string[:i]) > len(longest) else longest

    return longest

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abc") == "a", "Nothing"
    assert longest_palindromic("1") == "1", "One character"
