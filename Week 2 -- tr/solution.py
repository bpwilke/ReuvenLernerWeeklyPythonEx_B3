def tr(instr, deststr):
    ## quick check on whether either input translation is an empty string -- if note raise TypeError
    if instr == '' or deststr == '':
        raise TypeError

    ## check if input and destination strings are not same length -- to accomodate the "cover" case
    if len(instr) != len(deststr):
        lastcharacter = deststr[-1]
        for _ in range(len(instr) - len(deststr)):
            # add the last character of the input string
            deststr += lastcharacter
    
    # Reuven solved this by using dict(zip(instr, deststr)) 
    #
    
    ## start the string replacement algorithm (encapsulate in a Function for returning)
    def returnFunction(characters):
        ## convert the input phrase (str) to a list
        outputString = list(characters)
        ## for each of the characters in the translation input
        for char_idx, inchar in enumerate(instr):
            ## check to see if each character in our input phrase matches the current translation input character
            for phrase_idx, character in enumerate(characters):
                ## if it does -> replace it with the destination character
                if character == inchar:
                    outputString[phrase_idx] = deststr[char_idx]   ## Since Reuven used a dict() in his solution. He used deststr.get(character, character) here
        ## put our string back together from list and return it
        return ''.join(outputString)
    return returnFunction 

def main():
    vowels_to_y = tr('aeiou', 'y')
    print(vowels_to_y('the quick brown fox jumps over the lazy dog'))

if __name__ == '__main__':
    main()

