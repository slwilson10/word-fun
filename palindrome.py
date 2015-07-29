def main():
  # User enters a string 
  word = raw_input('Eneter the word you would like to see if palindrome: ' )
  # Creates a empty list for the reversed string
  palindrome_word = []
  # Loops through the entered word backwards
  for l in range(len(word)-1, -1, -1):
    # Appends the letter to the list
    palindrome_word.append(word[l])
  # Joins the list into a string 
  palindrome_word = "".join(palindrome_word)
  # If reversed string is equal to string
  if word == palindrome_word:
    print word
    print palindrome_word
    print "This is a Palindrome"
  # If not
  else:
    print word
    print palindrome_word
    print "This is not a Palindrome"
 

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()