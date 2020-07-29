class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return(input_str[::-1])

    def is_english_vowel(self, ch):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
        or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
            return True
        else:
            return False

    def find_longest_word(self, sen):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        sen=list(sen.split(" "))
        lensen=[]
        for i in sen:
            lensen.append(len(i))

        return sen[lensen.index(max(lensen))]

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        text=list(text.split(" "))
        lentext=[]
        for i in text:
            lentext.append(len(i))
        return lentext
