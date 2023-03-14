## Some VIM shortcuts
````sh
- ESC   # From Visual, Insert or Command line mode tape ESC to return to Nomrmal mode

- h     # Move left
- j     # Move down
- k     # Move Up
- l     # Move right

- w     # Move you forward one word
- b     # Move you at the begenning of the current word
- e     # Move to the end of current word
- gg    # Move to top of file
- G     # Move to the button of file

- y     # Copy the highlighted text to the buffer
- yw    # Copy the word of text
- yy    # Copy line of text
- x     # Paste
- x     # Delete character
- dd    # Delete line
````
### Normal to Insert mode : Use i or I, a or A or o or O
- i     # Before cursor
- I     # Before line

- a     # After cursor
- A     # End of line

- o     # New line below 
- O     # New line above

### Normal to Insert mode : Use v or V, or Ctl-v
- v     # By Character
- V     # By line
- Ctl-v # Visual block

### Normal to Command line : Use : or / or ?
- :     # Execute command
- /     # Search down
- ?     # Search up
- :!    # Filter command

- help  # Documentation
- q     # Close the curent buffer
- w     # Save buffer
- e     # Open file
- new   # New buffer
- sav   # Save the current buffer

### Search
- /     # Search ahead
- ?     # Search back
- n     # Next match
- N        # Previous Match (go back)
- s/the_word_we_are_searching_for/the_word_that_we_are_goint_to_replace_with/g
- %s/the_word_we_are_searching_for/the_word_that_we_are_goint_to_replace_with/g # Remplace all the occurence

### Configuration
;set ruler
~/.vimrc

To paste line, tape in the command line set_paste and paste at the right location.
