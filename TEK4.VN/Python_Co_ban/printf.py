# Define function
def printf(*args, sep = " ", end =""):
    str=sep.join(args)
    print(str+end)
    return len(args)

#Call function
one_word = printf("learn")
print(one_word)

many_words = printf("learn", "python", "with", "tek4.vn")
print(many_words)

words_with_sep= printf("learn", "python", "with", "tek4.vn", sep = "_")
print(words_with_sep)

words_with_end= printf("learn","python", "with","tek4.vn",sep="_",end=".")
print(words_with_end)