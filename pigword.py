def main():
  # User enters a string to be reversed
  word = input('Enter the word you would like to have in pig latin: ' )
  # Creates a empty list for the reversed string
  pig_word = []
  pig_word.append(word[1:])
  pig_word.append('-')
  pig_word.append(word[0])
  pig_word.append('ay')

    
  # Joins the list into a string and prints
  print ("".join(pig_word))
 

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()