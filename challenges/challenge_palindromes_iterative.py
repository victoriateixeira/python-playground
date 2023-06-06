def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    result = False

    for i in range((len(word) + 1) // 2):
        if word[i] == word[len(word) - 1 - i] or len(word) == 2:
            result = True
        else:
            result = False
            break

    return result
