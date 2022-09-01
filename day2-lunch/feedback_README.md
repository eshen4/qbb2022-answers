Exercise 1: You're off to a really good start with this! A couple of small notes:
  * A couple of times in your `bed_parser.py` script, you have a comment like this `#if field length is equal to index 8 (9 columns)` when refering to code `if j ==8`. Here, you're not actually checking the lengths of the fields variable. To do that you would have to do `if fieldN == 8`. Rather, you're checking whether we're currently looking at the 8th field. We're looping through the fields, but we want to do different things for each field. So we're asking "Hey, are we currently looking at field[8]? Okay do this thing. Are we instead looking at field[9]? Do this other thing."
  *  For the RGB field, I think we want to convert the rgb values to ints. Right now, it looks like you're just leaving them as strings
  * Nice work using list comprehension for fields 10 and 11!


Really good work!
