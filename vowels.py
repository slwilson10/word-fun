def main():
  # User enters a string to count the vowels
  word = raw_input('Enter the word you would like to count the vowels: ' )
  # Creates a list full of vowels 
  vowels = ['a','e','i','o','u']
  # Creates a empty list for the vowels found
  vowels_in_word = []
  # Loops through the word and discovers the vowels
  for l in word:
    # Appends list if vowels are found
    if l in vowels:
      vowels_in_word.append(l)
      
  
    
  # Prints the sum of vowels found
  print 'This is how many vowels in this word: '
  print len(vowels_in_word)
 

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()