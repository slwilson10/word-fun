def main():
  # User enters a string to be reversed
  word = input('Eneter the word you would like to reverse: ' )
  # Creates a empty list for the reversed string
  reverse_word = []
  # Loops through the entered word backwards
  for l in range(len(word)-1, -1, -1):
    # Appends the letter to the list
    reverse_word.append(word[l])
  # Joins the list into a string and prints
  print("".join(reverse_word))
 

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()