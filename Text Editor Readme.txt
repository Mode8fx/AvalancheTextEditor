HOW TO USE THIS SCRIPT:

I know this isn't the most user-friendly script, but I only made it for myself. All you really need to know is that you can edit the function "prepareNewTextSequences()" (which contains the original game's dialogue by default), and it will edit the appropriate text in the game. Also, replace "romFile" near the top of the script (romFile = "D:\\My Rom Location\\Kirby's Avalanche (USA).sfc") with the location of your Kirby's Avalanche (USA) rom.

Your rom WILL be modified (but only if it's a valid original Kirby's Avalanche (USA) rom), so make a copy first!



Take the following text sequence representing dialogue from the original game, for example:

textSequences.append(TextSequence("Waddle Dee", 105, 40))
textSequences[0].addTextBox(TextBox("Waddle Dee 1", 0x1B5BA, 31, 10, 2, 10, 6, box_w=18, box_h=6))
textSequences[0].textBoxes[0].addLine("Hi, Waddle Dee!", 3, 11)
textSequences[0].textBoxes[0].addLine("Are you ready?!?", 3, 13)
textSequences[0].addTextBox(TextBox("Waddle Dee 2", 0x1B5F0, 52, 20, 9, 2, 6, box_w=19, box_h=10))
textSequences[0].textBoxes[1].addLine("Umm, can we just", 10, 3)
textSequences[0].textBoxes[1].addLine("walk together?", 10, 5)
textSequences[0].textBoxes[1].addLine("The forest scares", 10, 7)
textSequences[0].textBoxes[1].addLine("me...", 10, 9)
textSequences[0].addTextBox(TextBox("Waddle Dee 3", 0x1B64B, 22, 10, 3, 10, 6, box_w=18, box_h=6))
textSequences[0].textBoxes[2].addLine("Sorry, rules are", 4, 11)
textSequences[0].textBoxes[2].addLine("rules!", 4, 13)



The first line creates a new TextSequence and should not be modified (the 105 represents the number of bytes used up by characters (letters, numbers, etc) in the sequence, while the 40 represents the number of additional bytes used by each line (5 bytes per line; this sequence has 8 lines). I do not know how to change the number of textboxes in a sequence.

The addTextBox() lines each create a new text box with the following information:
- Name of text box (used for your benefit only; not present in-game)
- The rom address at which the first line of the text box is initialized
- The number of bytes used up by characters
- The number of additional bytes used by each line
- X position of the box (top-left corner)
- Y position of the box (top-left corner)
- Some sort of "box type"; I don't know exactly what it is, but you shouldn't change it
- Width of the box (optional)
- Height of the box (optional)

The addLine() lines each create a new line for the most recent text box, with the following information:
- Text
- X position of the text (top-left corner)
- Y position of the text (top-left corner)



Finally, each text box CANNOT contain more bytes than the original version of that text box. For example, the "Waddle Dee 1" text box:

textSequences[0].addTextBox(TextBox("Waddle Dee 1", 0x1B5BA, 31, 10, 2, 10, 6, box_w=18, box_h=6))
textSequences[0].textBoxes[0].addLine("Hi, Waddle Dee!", 3, 11)
textSequences[0].textBoxes[0].addLine("Are you ready?!?", 3, 13)

... must contain a maximum of 41 (31+10) bytes. That can be either 31 characters across two lines (which is what the original uses) (31 + (2*5) = 41), or 36 characters on a single line (36 + (1*5) = 41), or 26 characters across three lines (26 + (3*5) = 41), etc.

The program will warn you if your text is estimated to not fit within the desired textbox (meaning you should make the text box wider and/or taller), and will refuse to modify your rom if you use too many bytes.