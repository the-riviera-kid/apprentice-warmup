# Warmup Exercises

These are presented in no particular order of difficulty, but I've made a rough guess at how hard you will find them. For each one, make a git repository (online if you like), a virtual environment, and write tests.

1. *EASY* Write a FizzBuzz function that takes a number, and returns a list of strings, each containing one "number". What's FizzBuzz? https://en.wikipedia.org/wiki/Fizz_buzz

2. *EASY* Write a function that takes a string, and returns True if that string is a palindrome.

3. *MEDIUM* Write a function that takes a string, and returns True if that string is a palindrome, or if it's *nearly* a palindrome. "Nearly a palindrome" is defined as "a palindrome with extra letters as the end." Minimum length of the palindrome part is 3 characters.
    ```
    poop -> True
    crap -> False
    Madam, I'm Adam -> True
    tent -> False
    tenet -> True
    tenets -> True (extra letters at the end, so it's nearly a palindrome)
    babble -> True (extra letters at the end, "bab" is a palindrome)
    levelling -> True (extra letters at the end)
    lotto -> False ("otto" is palindromic, but the extra letter is at the *start*, so it doesn't count.)
    aardvark -> False (i suppose "aa" is a palindrome, but it's too short to count.)
    ```

4. *EASY* There was a popular thing going around the internet a while ago; how to find out your Star Wars name! For the first part, you take the first three letters of your last name, and the first two letters of your first name. For the second part, you take the first two letters of your mother's maiden name, and the first three letters of the city where you were born.

    So, let's say my name is Dan van der Jackson, my mother's maiden name is O'Brien, and I was born in Edinburgh. In that case, my Star Wars name would be Jacda Obedi. Notice that punctuation is ignored, it's capitalized correctly, etc.

    Write a function to generate Star Wars Names. It should take a whole name, a maiden name, and a city name, and it should return a string containing the Star Wars Name. Call your module `star_wars.py`, and use this function signature:
    ```python
    def star_wars_name(name, maiden_name, city):
        pass # should return string
    ```
    Your code should not throw exceptions. In error conditions, (e.g. a maiden_name is not provided, the last name is 'Wu', etc) the function should use the largest portion of the name it can (so, empty string for no maiden name, and just the first two letters of 'Wu'.)

4. *HARD* Read the next exercise, but don't write the code. Write a suite of tests for it.
5. *MEDIUM* Write a function that takes as input a dictionary, and a target string. The input dictionary may be nested (i.e. contain other dictionaries). Return True if *any* dictionary in the tree contains a key matching the target string. Call your module `dictionary_search.py`, and the function signature should be:
    ```python
    def find_key(source_dictionary, target_string):
       pass # should return boolean
    ```

6. *EASY* Write a program to report on how many rude words Shakespeare ever used, i.e.:
    ```
    "fuck": 3
    "shit": 9
    "piss": 0
    "zounds": 3
    ```
    (I don't know what the actual numbers would be, you'll find out!)
    https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

7. *EASY* Write a program to print ASCII Font versions of any text you give it. i.e.:
    ```
    > python ascii-font.py A word
      *       * * *  ***  ***   ***
     * *      * * * *   * *  *  *  *
    *   *      * *  *   * *  *  *  *
    *****      * *  *   * ****  *  *
    *   *      * *   ***  *   * *** 
    ```

    Be as creative as you like! Don't use any external libraries or APIs.

8. *EASY* Write a function which takes a list of elements. Return a copy of the list with the same elements in the same order, _except_ all the instances of the number 0 (zero) have been moved to the end.
   ```
   [ 0, 1, 3, 0, "101", 101 ] -> [ 1, 3, "101", 101, 0, 0 ]
   ```

8. *EASY* Write a function which takes a list of numbers. Return the number of times that one element is equal to the next element. The list is circular; the last element is next to the first element. An element cannot be compared to itself.
   ```
   [ 2 ] -> 0
   [ 1, 1 ] -> 2
   [ 1, 1, 0 ] -> 1
   [ 4, 4, 7, 7, 4 ] -> 3
   ```

8. *EASY* Write a function which takes a square 2D grid, where every element is an integer. Return the number of elements where the value is equal to either the row index or the column index.
    ```
    9 9 9
    9 9 9
    9 9 9 -> 0

    0 9
    9 9 -> 1

    0 0 0
    0 0 0
    0 0 0 -> 5

    0 0 0
    0 1 1
    0 1 2 -> 9
    ```

8. *MEDIUM* Pyramid Numbers! Write a program which takes an integer, _size_ on the command line. The program should output a square of numbers, representing a _size_ x _size_ pyramid, viewed from above. Each number represents the height of that layer of stones. Each square of stones should get higher as they approach the center.
    ```
    python pyramids.py 3
    111
    121
    111

    python pyramids.py 7
    1111111
    1222221
    1233321
    1234321
    1233321
    1222221
    1111111
    ```

8. *MEDIUM* Modify the pyramids program to take an additional argument:
   ```
   python pyramids.py --to-pgm <FILENAME>.pgm 7
   ```
   If the `--to-pgm` argument is given, the program should output a representation of the pyramid in PGM format to the given filename. It should do this in addition to outputting the pyramid to the terminal.

   The PGM (Portable Graymap) format is a very simple graphics format which can be loaded in most image viewers or graphics programs. You can read all about it on Wikipedia: https://en.wikipedia.org/wiki/Netpbm

   This repository contains a sample PGM, generated with a pyramid of size 7.

8. *MEDIUM* Add an additional argument to the pyramids program, `--scale n`. Your pyramid images will have been quite small, and require you to zoom in. The new `--scale n` argument allows you to specify a scaling factor; a number by which to multiply every pixel, making a "zoomed in" effect. This should affect both the terminal view, and the generated PGM file.
   ```
   python pyramids.py --to-pgm my_file.pgm --scale 2 3
   111111
   111111
   112211
   112211
   111111
   111111
   ```

8. *HARD* Mathematical snowflakes! When I was about ten years old, we had a substitute teacher, and I think she wanted to keep us busy - as well as teach us how to follow instructions. She gave us this game called Mathematical Snowflakes. You get some graph paper, and some colored pens. You color in one square in the middle of the paper. Then, in a different color, you color in every square that touches an existing square on only one side. Then, in a different color, you color in every square that touches an existing square on only one side. Then, and you'll never believe this, but in a different color, you color in every square that touches an existing square on only one side. You keep going until you're bored, or the teacher is bored.

   If you do this, you end up with some very pretty patterns. Because I'm a nerd, I did this for _hours_ as a boy. I found out later that technically, this is a class of celluar automata called the Packard Snowflake. If you look in the `packard_snowflakes` directory of this repository, you'll find photographs of the first eight steps of the snowflake, and yes I did color them in by hand.

   Your exercise is to write a program to print out a mathematical snowflake. Take a number on the command line which is the number of generations to run, and then output it to the terminal. Hint; you can use the `█` character to represent a colored-in square.

   Is that too easy? Bonus points available:
   * Save the snowflake to a PGM file, as above.
   * Use the Blessed library to print the snowflakes out in different colors.
   * Use Blessed, and animate the printing of the snowflake; print out the first generation, wait a second, print the next generation, wait, print the next...
   * Save the snowflake as a PPM file; i.e. the color version of PGM https://en.wikipedia.org/wiki/Netpbm
   * Look up 'cellular automata'. Do you see any famous examples you recognize? Do you see similarities between that and the snowflakes? Could you generalize your program to produce both?

8. *MEDIUM* In the `football_scores` module in this repository, you'll find a `get_league_table` function. Unit test it thoroughly. If there are bugs, fix them. Once it's correct, refactor it to make it clearer.

8. *HARD* Write a Connect 4 game!

8. *FUCK ME DEAD* Write a Base64 encode/decode program. Don't use any external libraries or APIs. Also, don't use the Python `base64` module; you already know how to import and call functions, that's not what you should practice here. :)

   You probably want to start by reading the wikipedia page on the topic: https://en.wikipedia.org/wiki/Base64

   Your program should be interoperable with the `base64` command line tool; your tool should decode anything it encodes, and vice versa.


