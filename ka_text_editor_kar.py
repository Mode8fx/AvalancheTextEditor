# This version of the text editor contains changes implemented in "Kirby's Avalanche: Rewritten"

import os
from os import path
import sys
import math
import shutil
import binascii

startAddress = 0x1B5A0
endAddress = 0x1C38F

########################
# Edit below this line #
########################

romFile = "D:\\Kirby's Avalanche - Rewritten\\Kirby's Avalanche (USA).sfc"
replaceAvalancheWithPuyo = False # If True, then all uses of "Avalanche" will be replaced with "Puyo Puyo"

def prepareNewTextSequences():
	textSequences.append(TextSequence("Waddle Dee", 105, 40))
	textSequences[0].addTextBox(TextBox("Waddle Dee 1", 0x1B5BA, 31, 10, 2, 10, 6, 19, 6))
	textSequences[0].textBoxes[0].addLine("Wanna play a game", 3, 11)
	textSequences[0].textBoxes[0].addLine("of Avalanche?", 3, 13)
	textSequences[0].addTextBox(TextBox("Waddle Dee 2", 0x1B5F0, 52, 20, 9, 2, 6, 19, 10))
	textSequences[0].textBoxes[1].addLine("Umm, I don't know", 10, 3)
	textSequences[0].textBoxes[1].addLine("how to play...", 10, 5)
	textSequences[0].textBoxes[1].addLine("Can you teach", 10, 7)
	textSequences[0].textBoxes[1].addLine("me?", 10, 9)
	textSequences[0].addTextBox(TextBox("Waddle Dee 3", 0x1B64B, 22, 10, 3, 10, 6, 18, 6))
	textSequences[0].textBoxes[2].addLine("Don't worry,", 4, 11)
	textSequences[0].textBoxes[2].addLine("it's easy!", 4, 13)

	textSequences.append(TextSequence("Bronto Burt", 104, 35))
	textSequences[1].addTextBox(TextBox("Bronto Burt 1", 0x1B679, 36, 15, 11, 4, 6, 17, 8))
	textSequences[1].textBoxes[0].addLine("Ah HA!!! I've", 12, 5)
	textSequences[1].textBoxes[0].addLine("found a new", 12, 7)
	textSequences[1].textBoxes[0].addLine("opponent!!", 12, 9)
	textSequences[1].addTextBox(TextBox("Bronto Burt 2", 0x1B6BB, 51, 15, 2, 8, 6, 21, 8))
	textSequences[1].textBoxes[1].addLine("Bronto Burt! Do", 3, 9)
	textSequences[1].textBoxes[1].addLine("you want to", 3, 11)
	textSequences[1].textBoxes[1].addLine("play, too?", 3, 13)
	textSequences[1].addTextBox(TextBox("Bronto Burt 3", 0x1B70C, 17, 5, 10, 8, 6, 19, 4))
	textSequences[1].textBoxes[2].addLine("Not PLAY. Battle!", 11, 9)

	textSequences.append(TextSequence("Waddle Doo", 100, 30))
	textSequences[2].addTextBox(TextBox("Waddle Doo 1", 0x1B72F, 82, 25, 10, 4, 6, 20, 12))
	textSequences[2].textBoxes[0].addLine("You've done well", 11, 5)
	textSequences[2].textBoxes[0].addLine("so far, Kirby...", 11, 7)
	textSequences[2].textBoxes[0].addLine("Now I, Waddle Doo,", 11, 9)
	textSequences[2].textBoxes[0].addLine("will be your final", 11, 11)
	textSequences[2].textBoxes[0].addLine("test!!", 11, 13)
	textSequences[2].addTextBox(TextBox("Waddle Doo 2", 0x1B7AD, 18, 5, 3, 12, 6, 20, 4))
	textSequences[2].textBoxes[1].addLine("Okay! I'm ready!", 4, 13)

	textSequences.append(TextSequence("Dedede Intro", 162, 50))
	textSequences[3].addTextBox(TextBox("Dedede Intro 1", 0x1B7D1, 76, 25, 7, 2, 6, 19, 12))
	textSequences[3].textBoxes[0].addLine("Congratulations!", 8, 3)
	textSequences[3].textBoxes[0].addLine("You're a fast", 8, 5)
	textSequences[3].textBoxes[0].addLine("learner... but", 8, 7)
	textSequences[3].textBoxes[0].addLine("don't get too", 8, 9)
	textSequences[3].textBoxes[0].addLine("cocky!", 8, 11)
	textSequences[3].addTextBox(TextBox("Dedede Intro 2", 0x1B849, 86, 25, 6, 2, 6, 21, 12))
	textSequences[3].textBoxes[1].addLine("Hurry through the", 7, 3)
	textSequences[3].textBoxes[1].addLine("forest and meet", 7, 5)
	textSequences[3].textBoxes[1].addLine("me at the Fountain", 7, 7)
	textSequences[3].textBoxes[1].addLine("of Dreams for a", 7, 9)
	textSequences[3].textBoxes[1].addLine("REAL challenge!", 7, 11)

	textSequences.append(TextSequence("Poppy Bros. Sr.", 154, 55))
	textSequences[4].addTextBox(TextBox("Poppy Bros. Sr. 1", 0x1B8CD, 31, 10, 10, 6, 6, 19, 6))
	textSequences[4].textBoxes[0].addLine("Hi, Kirby! Want a", 11, 7)
	textSequences[4].textBoxes[0].addLine("bomb sandwich?", 11, 9)
	textSequences[4].addTextBox(TextBox("Poppy Bros. Sr. 2", 0x1B903, 64, 25, 3, 4, 6, 20, 12))
	textSequences[4].textBoxes[1].addLine("Try it! I'll", 4, 5)
	textSequences[4].textBoxes[1].addLine("breathe in your", 4, 7)
	textSequences[4].textBoxes[1].addLine("bombs and send", 4, 9)
	textSequences[4].textBoxes[1].addLine("them right back", 4, 11)
	textSequences[4].textBoxes[1].addLine("at you!", 4, 13)
	textSequences[4].addTextBox(TextBox("Poppy Bros. Sr. 3", 0x1B96F, 59, 20, 9, 2, 6, 21, 10))
	textSequences[4].textBoxes[2].addLine("Okay...", 10, 3)
	textSequences[4].textBoxes[2].addLine("Instead of bombs,", 10, 5)
	textSequences[4].textBoxes[2].addLine("we'll fight with", 10, 7)
	textSequences[4].textBoxes[2].addLine("blobs! Avalanche!", 10, 9)

	textSequences.append(TextSequence("Whispy Woods", 87, 30))
	textSequences[5].addTextBox(TextBox("Whispy Woods 1", 0x1B9CF, 61, 20, 1, 6, 6, 20, 10))
	textSequences[5].textBoxes[0].addLine("Please be careful", 2, 7)
	textSequences[5].textBoxes[0].addLine("around my roots,", 2, 9)
	textSequences[5].textBoxes[0].addLine("can't you walk", 2, 11)
	textSequences[5].textBoxes[0].addLine("another way?", 2, 13)
	textSequences[5].addTextBox(TextBox("Whispy Woods 2", 0x1BA31, 26, 10, 2, 10, 6, 18, 6))
	textSequences[5].textBoxes[1].addLine("But I want some", 3, 11)
	textSequences[5].textBoxes[1].addLine("apple pie!", 3, 13)

	textSequences.append(TextSequence("Kabu", 113, 45))
	textSequences[6].addTextBox(TextBox("Kabu 1", 0x1BA62, 37, 15, 3, 8, 6, 17, 8))
	textSequences[6].textBoxes[0].addLine("Who blocked the", 4, 9)
	textSequences[6].textBoxes[0].addLine("path with this", 4, 11)
	textSequences[6].textBoxes[0].addLine("boulder?", 4, 13)
	textSequences[6].addTextBox(TextBox("Kabu 2", 0x1BAA7, 27, 10, 9, 10, 6, 20, 6))
	textSequences[6].textBoxes[1].addLine("Your journey ends", 10, 11)
	textSequences[6].textBoxes[1].addLine("here...", 10, 13)
	textSequences[6].addTextBox(TextBox("Kabu 3", 0x1BADB, 49, 20, 3, 6, 6, 19, 10))
	textSequences[6].textBoxes[2].addLine("OH!! Hi Kabu,", 4, 7)
	textSequences[6].textBoxes[2].addLine("are you ready for", 4, 9)
	textSequences[6].textBoxes[2].addLine("a game of", 4, 11)
	textSequences[6].textBoxes[2].addLine("Avalanche?", 4, 13)

	textSequences.append(TextSequence("Broom Hatter", 133, 50))
	textSequences[7].addTextBox(TextBox("Broom Hatter 1", 0x1BB31, 49, 15, 8, 8, 6, 21, 8))
	textSequences[7].textBoxes[0].addLine("Oh what a mess!", 9, 9)
	textSequences[7].textBoxes[0].addLine("Must I clean up", 9, 11)
	textSequences[7].textBoxes[0].addLine("this entire forest?", 9, 13)
	textSequences[7].addTextBox(TextBox("Broom Hatter 2", 0x1BB80, 58, 20, 3, 6, 6, 19, 10))
	textSequences[7].textBoxes[1].addLine("How are you gonna", 4, 7)
	textSequences[7].textBoxes[1].addLine("clean the whole", 4, 9)
	textSequences[7].textBoxes[1].addLine("forest with just", 4, 11)
	textSequences[7].textBoxes[1].addLine("a broom?", 4, 13)
	textSequences[7].addTextBox(TextBox("Broom Hatter 3", 0x1BBDF, 26, 15, 14, 8, 6, 13, 8))
	textSequences[7].textBoxes[2].addLine("Dust, dust,", 15, 9)
	textSequences[7].textBoxes[2].addLine("sweep...", 15, 11)
	textSequences[7].textBoxes[2].addLine("Huh?!??", 15, 13)

	textSequences.append(TextSequence("Squishy", 175, 55))
	textSequences[8].addTextBox(TextBox("Squishy 1", 0x1BC17, 52, 15, 7, 8, 6, 20, 8))
	textSequences[8].textBoxes[0].addLine("Get ready for an", 8, 9)
	textSequences[8].textBoxes[0].addLine("eight-armed", 8, 11)
	textSequences[8].textBoxes[0].addLine("Avalanche, Kirby!", 8, 13)
	textSequences[8].addTextBox(TextBox("Squishy 2", 0x1BC69, 80, 25, 3, 4, 6, 21, 12))
	textSequences[8].textBoxes[1].addLine("We can play later,", 4, 5)
	textSequences[8].textBoxes[1].addLine("Squishy. I've", 4, 7)
	textSequences[8].textBoxes[1].addLine("got to get to", 4, 9)
	textSequences[8].textBoxes[1].addLine("the Dream", 4, 11)
	textSequences[8].textBoxes[1].addLine("Fountain!", 4, 13)
	textSequences[8].addTextBox(TextBox("Squishy 3", 0x1BCE5, 43, 15, 10, 8, 6, 19, 8))
	textSequences[8].textBoxes[2].addLine("But King Dedede's", 11, 9)
	textSequences[8].textBoxes[2].addLine("orders... Get", 11, 11)
	textSequences[8].textBoxes[2].addLine("back here!!", 11, 13)

	textSequences.append(TextSequence("Lololo & Lalala", 100, 35))
	textSequences[9].addTextBox(TextBox("Lololo & Lalala 1", 0x1BD2E, 57, 20, 3, 6, 6, 21, 10))
	textSequences[9].textBoxes[0].addLine("To get this far you", 4, 7)
	textSequences[9].textBoxes[0].addLine("must have", 4, 9)
	textSequences[9].textBoxes[0].addLine("a-MAZE-ing skill,", 4, 11)
	textSequences[9].textBoxes[0].addLine("ha ha ha!!", 4, 13)
	textSequences[9].addTextBox(TextBox("Lololo & Lalala 2", 0x1BD8E, 43, 15, 11, 8, 6, 18, 8))
	textSequences[9].textBoxes[1].addLine("Oh yeah? Try and", 12, 9)
	textSequences[9].textBoxes[1].addLine("figure your way", 12, 11)
	textSequences[9].textBoxes[1].addLine("out of this!", 12, 13)

	textSequences.append(TextSequence("Bugzzy", 37, 15))
	textSequences[10].addTextBox(TextBox("Bugzzy 1", 0x1BDD7, 18, 5, 7, 10, 6, 20, 4))
	textSequences[10].textBoxes[0].addLine("ROOAAAAAAARRR!!!!!", 8, 11)
	textSequences[10].addTextBox(TextBox("Bugzzy 2", 0x1BDFD, 19, 10, 3, 12, 6, 26, 4))
	# textSequences[10].textBoxes[1].addLine("Oh, I'm soooo", 4, 11) # I'm not going to use this line
	textSequences[10].textBoxes[1].addLine("I'm not scared of you!", 4, 13)

	textSequences.append(TextSequence("Paint Roller", 174, 60))
	textSequences[11].addTextBox(TextBox("Paint Roller 1", 0x1BE27, 36, 10, 9, 10, 6, 20, 6))
	textSequences[11].textBoxes[0].addLine("Let me paint you a", 10, 11)
	textSequences[11].textBoxes[0].addLine("lovely portrait...", 10, 13)
	textSequences[11].addTextBox(TextBox("Paint Roller 2", 0x1BE62, 19, 10, 3, 10, 6, 15, 6))
	textSequences[11].textBoxes[1].addLine("Oh, how sweet", 4, 11)
	textSequences[11].textBoxes[1].addLine("of yo-", 4, 13)
	textSequences[11].addTextBox(TextBox("Paint Roller 3", 0x1BE8C, 33, 10, 10, 10, 6, 19, 6))
	textSequences[11].textBoxes[2].addLine("... of you losing", 11, 11)
	textSequences[11].textBoxes[2].addLine("to me, HA HA HA!", 11, 13)
	textSequences[11].addTextBox(TextBox("Paint Roller 4", 0x1BEC4, 57, 20, 3, 6, 6, 19, 10))
	textSequences[11].textBoxes[3].addLine("Hey, that's not", 4, 7)
	textSequences[11].textBoxes[3].addLine("lovely!... And", 4, 9)
	textSequences[11].textBoxes[3].addLine("that's not gonna", 4, 11)
	textSequences[11].textBoxes[3].addLine("happen!", 4, 13)
	textSequences[11].addTextBox(TextBox("Paint Roller 5", 0x1BF22, 29, 10, 10, 10, 6, 19, 6))
	textSequences[11].textBoxes[4].addLine("See what the", 11, 11)
	textSequences[11].textBoxes[4].addLine("MASTER can do!!", 11, 13)

	textSequences.append(TextSequence("Heavy Mole", 130, 45))
	textSequences[12].addTextBox(TextBox("Heavy Mole 1", 0x1BF56, 59, 20, 11, 6, 6, 18, 10))
	textSequences[12].textBoxes[0].addLine("I am Heavy Mole,", 12, 7)
	textSequences[12].textBoxes[0].addLine("watch while I", 12, 9)
	textSequences[12].textBoxes[0].addLine("UNDERMINE your", 12, 11)
	textSequences[12].textBoxes[0].addLine("precious dream!!", 12, 13)
	textSequences[12].addTextBox(TextBox("Heavy Mole 2", 0x1BFB8, 71, 25, 3, 4, 6, 21, 12))
	textSequences[12].textBoxes[1].addLine("There's the", 4, 5)
	textSequences[12].textBoxes[1].addLine("Fountain of", 4, 7)
	textSequences[12].textBoxes[1].addLine("Dreams... I'm gonna", 4, 9)
	textSequences[12].textBoxes[1].addLine("keep going and win", 4, 11)
	textSequences[12].textBoxes[1].addLine("that Cup!", 4, 13)

	textSequences.append(TextSequence("Mr. Shine & Mr. Bright", 152, 50))
	textSequences[13].addTextBox(TextBox("Mr. Shine & Mr. Bright 1", 0x1C02B, 34, 10, 9, 4, 6, 20, 6))
	textSequences[13].textBoxes[0].addLine("We rule both the", 10, 5)
	textSequences[13].textBoxes[0].addLine("night and the day!", 10, 7)
	textSequences[13].addTextBox(TextBox("Mr. Shine & Mr. Bright 2", 0x1C05F, 42, 15, 9, 3, 6, 20, 8))
	textSequences[13].textBoxes[1].addLine("That leaves no", 10, 4)
	textSequences[13].textBoxes[1].addLine("time for you,", 10, 6)
	textSequences[13].textBoxes[1].addLine("Kirby! Begone!!", 10, 8)
	textSequences[13].addTextBox(TextBox("Mr. Shine & Mr. Bright 3", 0x1C0A7, 76, 25, 1, 4, 6, 19, 12))
	textSequences[13].textBoxes[2].addLine("I'm always ready", 2, 5)
	textSequences[13].textBoxes[2].addLine("to battle, day or", 2, 7)
	textSequences[13].textBoxes[2].addLine("night! I can take", 2, 9)
	textSequences[13].textBoxes[2].addLine("you both on at", 2, 11)
	textSequences[13].textBoxes[2].addLine("any time.", 2, 13)

	textSequences.append(TextSequence("Kracko", 114, 40))
	textSequences[14].addTextBox(TextBox("Kracko 1", 0x1C11F, 65, 20, 9, 2, 6, 20, 10))
	textSequences[14].textBoxes[0].addLine("KRRR-RACKK!!!!", 10, 3)
	textSequences[14].textBoxes[0].addLine("Dance to my deadly", 10, 5)
	textSequences[14].textBoxes[0].addLine("music, or fry like", 10, 7)
	textSequences[14].textBoxes[0].addLine("a moth! HA HA!!", 10, 9)
	textSequences[14].addTextBox(TextBox("Kracko 2", 0x1C187, 49, 20, 3, 6, 6, 21, 10))
	textSequences[14].textBoxes[1].addLine("Your lightning", 4, 7)
	textSequences[14].textBoxes[1].addLine("can't match my", 4, 9)
	textSequences[14].textBoxes[1].addLine("Avalanche", 4, 11)
	textSequences[14].textBoxes[1].addLine("speed!", 4, 13)

	textSequences.append(TextSequence("Meta Knight", 109, 40))
	textSequences[15].addTextBox(TextBox("Meta Knight 1", 0x1C1DF, 32, 10, 11, 8, 6, 18, 6))
	textSequences[15].textBoxes[0].addLine("None shall pass!", 12, 9)
	textSequences[15].textBoxes[0].addLine("En garde, Kirby!", 12, 11)
	textSequences[15].addTextBox(TextBox("Meta Knight 2", 0x1C216, 21, 10, 3, 10, 6, 15, 6))
	textSequences[15].textBoxes[1].addLine("But I have no", 4, 11)
	textSequences[15].textBoxes[1].addLine("sword!?!", 4, 13)
	textSequences[15].addTextBox(TextBox("Meta Knight 3", 0x1C242, 56, 20, 9, 4, 6, 20, 10))
	textSequences[15].textBoxes[2].addLine("So be it... then", 10, 5)
	textSequences[15].textBoxes[2].addLine("prepare for a", 10, 7)
	textSequences[15].textBoxes[2].addLine("legendary", 10, 9)
	textSequences[15].textBoxes[2].addLine("Avalanche battle!!", 10, 11)

	textSequences.append(TextSequence("King Dedede", 134, 40))
	textSequences[16].addTextBox(TextBox("King Dedede 1", 0x1C2A1, 54, 15, 8, 6, 6, 21, 8))
	textSequences[16].textBoxes[0].addLine("Kirby! You may've", 9, 7)
	textSequences[16].textBoxes[0].addLine("bested my minions", 9, 9)
	textSequences[16].textBoxes[0].addLine("but your time's up.", 9, 11)
	textSequences[16].addTextBox(TextBox("King Dedede 2", 0x1C2F0, 36, 10, 8, 6, 6, 21, 8))
	textSequences[16].textBoxes[1].addLine("The Dream Fountain", 9, 7)
	textSequences[16].textBoxes[1].addLine("Cup will be mine!!", 9, 9)
	textSequences[16].addTextBox(TextBox("King Dedede 3", 0x1C32B, 44, 15, 3, 8, 6, 18, 8))
	textSequences[16].textBoxes[2].addLine("The final", 4, 9)
	textSequences[16].textBoxes[2].addLine("battle... Okay!", 4, 11)
	textSequences[16].textBoxes[2].addLine("Let's do this!!", 4, 13)

########################
# Edit above this line #
########################

textSequences = []
textSequenceIndex = 0

romToDecoded = {
	chr(0x46) : '\'',
	'F'  : '\'',
	'G'  : '\'',
	'@'  : '!',
	' '  : 'A',
	'!'  : 'B',
	'"'  : 'C',
	'#'  : 'D',
	'$'  : 'E',
	'%'  : 'F',
	'&'  : 'G',
	'\'' : 'H',
	'('  : 'I',
	')'  : 'J',
	'*'  : 'K',
	'+'  : 'L',
	','  : 'M',
	'-'  : 'N',
	'.'  : 'O',
	'/'  : 'P',
	'0'  : 'Q',
	'1'  : 'R',
	'2'  : 'S',
	'3'  : 'T',
	'4'  : 'U',
	'5'  : 'V',
	'6'  : 'W',
	'7'  : 'X',
	'8'  : 'Y',
	'9'  : 'Z',
	':'  : ',',
	';'  : '.',
	'?'  : '?',
	'`'  : 'a',
	'a'  : 'b',
	'b'  : 'c',
	'c'  : 'd',
	'd'  : 'e',
	'e'  : 'f',
	'f'  : 'g',
	'g'  : 'h',
	'h'  : 'i',
	'i'  : 'j',
	'j'  : 'k',
	'k'  : 'l',
	'l'  : 'm',
	'm'  : 'n',
	'n'  : 'o',
	'o'  : 'p',
	'p'  : 'q',
	'q'  : 'r',
	'r'  : 's',
	's'  : 't',
	't'  : 'u',
	'u'  : 'v',
	'v'  : 'w',
	'w'  : 'x',
	'x'  : 'y',
	'y'  : 'z',
}

decodedToRom = {
	'\'' : chr(0x46),
	# '\'' : 'F',
	# '\'' : 'G',
	'!'  : '@',
	'A'  : ' ',
	'B'  : '!',
	'C'  : '"',
	'D'  : '#',
	'E'  : '$',
	'F'  : '%',
	'G'  : '&',
	'H'  : '\'',
	'I'  : '(',
	'J'  : ')',
	'K'  : '*',
	'L'  : '+',
	'M'  : ',',
	'N'  : '-',
	'O'  : '.',
	'P'  : '/',
	'Q'  : '0',
	'R'  : '1',
	'S'  : '2',
	'T'  : '3',
	'U'  : '4',
	'V'  : '5',
	'W'  : '6',
	'X'  : '7',
	'Y'  : '8',
	'Z'  : '9',
	','  : ':',
	'.'  : ';',
	'?'  : '?',
	'a'  : '`',
	'b'  : 'a',
	'c'  : 'b',
	'd'  : 'c',
	'e'  : 'd',
	'f'  : 'e',
	'g'  : 'f',
	'h'  : 'g',
	'i'  : 'h',
	'j'  : 'i',
	'k'  : 'j',
	'l'  : 'k',
	'm'  : 'l',
	'n'  : 'm',
	'o'  : 'n',
	'p'  : 'o',
	'q'  : 'p',
	'r'  : 'q',
	's'  : 'r',
	't'  : 's',
	'u'  : 't',
	'v'  : 'u',
	'w'  : 'v',
	'x'  : 'w',
	'y'  : 'x',
	'z'  : 'y',
}

def verifyRomIntegrity():
	if not path.isfile(romFile):
		print("Kirby's Avalanche (USA) rom file not found. Quitting.")
		sys.exit()
	with open(romFile, "rb") as inputFile:
		fileBytes = inputFile.read()
	correctHash = "21E658B8"
	fileHash = str(hex(binascii.crc32(fileBytes)))[2:].zfill(8).upper()
	if correctHash != fileHash:
		print("Invalid rom; CRC32 does not match expected value.\n\nExpected: "+correctHash+"\nGot: "+fileHash)
		sys.exit()

def prepareOriginalTextSequences():
	textSequences.append(TextSequence("Waddle Dee", 105, 40))
	textSequences[0].addTextBox(TextBox("Waddle Dee 1", 0x1B5BA, 31, 10, 2, 10, 6, 18, 6))
	textSequences[0].textBoxes[0].addLine("Hi, Waddle Dee!", 3, 11)
	textSequences[0].textBoxes[0].addLine("Are you ready?!?", 3, 13)
	textSequences[0].addTextBox(TextBox("Waddle Dee 2", 0x1B5F0, 52, 20, 9, 2, 6, 19, 10))
	textSequences[0].textBoxes[1].addLine("Umm, can we just", 10, 3)
	textSequences[0].textBoxes[1].addLine("walk together?", 10, 5)
	textSequences[0].textBoxes[1].addLine("The forest scares", 10, 7)
	textSequences[0].textBoxes[1].addLine("me...", 10, 9)
	textSequences[0].addTextBox(TextBox("Waddle Dee 3", 0x1B64B, 22, 10, 3, 10, 6, 18, 6))
	textSequences[0].textBoxes[2].addLine("Sorry, rules are", 4, 11)
	textSequences[0].textBoxes[2].addLine("rules!", 4, 13)

	textSequences.append(TextSequence("Bronto Burt", 104, 35))
	textSequences[1].addTextBox(TextBox("Bronto Burt 1", 0x1B679, 36, 15, 11, 4, 6, 17, 8))
	textSequences[1].textBoxes[0].addLine("Ah HA!!! I have", 12, 5)
	textSequences[1].textBoxes[0].addLine("found my next", 12, 7)
	textSequences[1].textBoxes[0].addLine("victim!!", 12, 9)
	textSequences[1].addTextBox(TextBox("Bronto Burt 2", 0x1B6BB, 51, 15, 2, 8, 6, 21, 8))
	textSequences[1].textBoxes[1].addLine("Bronto Burt you", 3, 9)
	textSequences[1].textBoxes[1].addLine("bully, the pleasure", 3, 11)
	textSequences[1].textBoxes[1].addLine("will be all mine.", 3, 13)
	textSequences[1].addTextBox(TextBox("Bronto Burt 3", 0x1B70C, 17, 5, 10, 8, 6, 19, 4))
	textSequences[1].textBoxes[2].addLine("Shut up and play!", 11, 9)

	textSequences.append(TextSequence("Waddle Doo", 100, 30))
	textSequences[2].addTextBox(TextBox("Waddle Doo 1", 0x1B72F, 82, 25, 10, 4, 6, 20, 12))
	textSequences[2].textBoxes[0].addLine("You did not treat", 11, 5)
	textSequences[2].textBoxes[0].addLine("Waddle Dee with", 11, 7)
	textSequences[2].textBoxes[0].addLine("respect... Now I,", 11, 9)
	textSequences[2].textBoxes[0].addLine("Waddle Doo will", 11, 11)
	textSequences[2].textBoxes[0].addLine("repay you in kind!", 11, 13)
	textSequences[2].addTextBox(TextBox("Waddle Doo 2", 0x1B7AD, 18, 5, 3, 12, 6, 20, 4))
	textSequences[2].textBoxes[1].addLine("I don't think so!!", 4, 13)

	textSequences.append(TextSequence("Dedede Intro", 162, 50))
	textSequences[3].addTextBox(TextBox("Dedede Intro 1", 0x1B7D1, 76, 25, 7, 2, 6, 19, 12))
	textSequences[3].textBoxes[0].addLine("Congratulations!", 8, 3)
	textSequences[3].textBoxes[0].addLine("You are a fast", 8, 5)
	textSequences[3].textBoxes[0].addLine("learner. I under-", 8, 7)
	textSequences[3].textBoxes[0].addLine("estimated your", 8, 9)
	textSequences[3].textBoxes[0].addLine("skill... MAYBE!", 8, 11)
	textSequences[3].addTextBox(TextBox("Dedede Intro 2", 0x1B849, 86, 25, 6, 2, 6, 21, 12))
	textSequences[3].textBoxes[1].addLine("Now hurry through", 7, 3)
	textSequences[3].textBoxes[1].addLine("the forest and join", 7, 5)
	textSequences[3].textBoxes[1].addLine("us at the Dream", 7, 7)
	textSequences[3].textBoxes[1].addLine("Fountain for the", 7, 9)
	textSequences[3].textBoxes[1].addLine("serious competition", 7, 11)

	textSequences.append(TextSequence("Poppy Bros. Sr.", 154, 55))
	textSequences[4].addTextBox(TextBox("Poppy Bros. Sr. 1", 0x1B8CD, 31, 10, 10, 6, 6, 19, 6))
	textSequences[4].textBoxes[0].addLine("Hi, Kirby! Want a", 11, 7)
	textSequences[4].textBoxes[0].addLine("bomb sandwich?", 11, 9)
	textSequences[4].addTextBox(TextBox("Poppy Bros. Sr. 2", 0x1B903, 64, 25, 3, 4, 6, 20, 12))
	textSequences[4].textBoxes[1].addLine("I'll breathe in", 4, 5)
	textSequences[4].textBoxes[1].addLine("your pathetic", 4, 7)
	textSequences[4].textBoxes[1].addLine("bombs and send", 4, 9)
	textSequences[4].textBoxes[1].addLine("them right back at", 4, 11)
	textSequences[4].textBoxes[1].addLine("you!", 4, 13)
	textSequences[4].addTextBox(TextBox("Poppy Bros. Sr. 3", 0x1B96F, 59, 20, 9, 2, 6, 21, 10))
	textSequences[4].textBoxes[2].addLine("Stalemate...", 10, 3)
	textSequences[4].textBoxes[2].addLine("Okay, let's compete", 10, 5)
	textSequences[4].textBoxes[2].addLine("in a quick game of", 10, 7)
	textSequences[4].textBoxes[2].addLine("Avalanche!", 10, 9)

	textSequences.append(TextSequence("Whispy Woods", 87, 30))
	textSequences[5].addTextBox(TextBox("Whispy Woods 1", 0x1B9CF, 61, 20, 1, 6, 6, 20, 10))
	textSequences[5].textBoxes[0].addLine("Please don't tread", 2, 7)
	textSequences[5].textBoxes[0].addLine("on my roots, it", 2, 9)
	textSequences[5].textBoxes[0].addLine("would not be a", 2, 11)
	textSequences[5].textBoxes[0].addLine("wise decision.", 2, 13)
	textSequences[5].addTextBox(TextBox("Whispy Woods 2", 0x1BA31, 26, 10, 2, 10, 6, 18, 6))
	textSequences[5].textBoxes[1].addLine("I feel like some", 3, 11)
	textSequences[5].textBoxes[1].addLine("apple pie!", 3, 13)

	textSequences.append(TextSequence("Kabu", 113, 45))
	textSequences[6].addTextBox(TextBox("Kabu 1", 0x1BA62, 37, 15, 3, 8, 6, 17, 8))
	textSequences[6].textBoxes[0].addLine("Who blocked the", 4, 9)
	textSequences[6].textBoxes[0].addLine("path with this", 4, 11)
	textSequences[6].textBoxes[0].addLine("boulder?", 4, 13)
	textSequences[6].addTextBox(TextBox("Kabu 2", 0x1BAA7, 27, 10, 9, 10, 6, 20, 6))
	textSequences[6].textBoxes[1].addLine("Your road to glory", 10, 11)
	textSequences[6].textBoxes[1].addLine("ends here", 10, 13)
	textSequences[6].addTextBox(TextBox("Kabu 3", 0x1BADB, 49, 20, 3, 6, 6, 19, 10))
	textSequences[6].textBoxes[2].addLine("OH!! Hi Kabu,", 4, 7)
	textSequences[6].textBoxes[2].addLine("are you ready for", 4, 9)
	textSequences[6].textBoxes[2].addLine("a game of", 4, 11)
	textSequences[6].textBoxes[2].addLine("Avalanche?", 4, 13)

	textSequences.append(TextSequence("Broom Hatter", 133, 50))
	textSequences[7].addTextBox(TextBox("Broom Hatter 1", 0x1BB31, 49, 15, 8, 8, 6, 21, 8))
	textSequences[7].textBoxes[0].addLine("Oh what a mess!", 9, 9)
	textSequences[7].textBoxes[0].addLine("Must I clean up", 9, 11)
	textSequences[7].textBoxes[0].addLine("this entire forest?", 9, 13)
	textSequences[7].addTextBox(TextBox("Broom Hatter 2", 0x1BB80, 58, 20, 3, 6, 6, 19, 10))
	textSequences[7].textBoxes[1].addLine("I'd worry more", 4, 7)
	textSequences[7].textBoxes[1].addLine("about cleaning up", 4, 9)
	textSequences[7].textBoxes[1].addLine("your Avalanche", 4, 11)
	textSequences[7].textBoxes[1].addLine("skills first.", 4, 13)
	textSequences[7].addTextBox(TextBox("Broom Hatter 3", 0x1BBDF, 26, 15, 14, 8, 6, 13, 8))
	textSequences[7].textBoxes[2].addLine("Dust, dust,", 15, 9)
	textSequences[7].textBoxes[2].addLine("sweep...", 15, 11)
	textSequences[7].textBoxes[2].addLine("Huh?!??", 15, 13)

	textSequences.append(TextSequence("Squishy", 175, 55))
	textSequences[8].addTextBox(TextBox("Squishy 1", 0x1BC17, 52, 15, 7, 8, 6, 20, 8))
	textSequences[8].textBoxes[0].addLine("I know what your", 8, 9)
	textSequences[8].textBoxes[0].addLine("dream is! But King", 8, 11)
	textSequences[8].textBoxes[0].addLine("Dedede was saying-", 8, 13)
	textSequences[8].addTextBox(TextBox("Squishy 2", 0x1BC69, 80, 25, 3, 4, 6, 21, 12))
	textSequences[8].textBoxes[1].addLine("Go meddle in", 4, 5)
	textSequences[8].textBoxes[1].addLine("someone else's", 4, 7)
	textSequences[8].textBoxes[1].addLine("affairs, Squishy,", 4, 9)
	textSequences[8].textBoxes[1].addLine("I've got to get to", 4, 11)
	textSequences[8].textBoxes[1].addLine("the Dream Fountain.", 4, 13)
	textSequences[8].addTextBox(TextBox("Squishy 3", 0x1BCE5, 43, 15, 10, 8, 6, 19, 8))
	textSequences[8].textBoxes[2].addLine("An eight-armed", 11, 9)
	textSequences[8].textBoxes[2].addLine("Avalanche for you", 11, 11)
	textSequences[8].textBoxes[2].addLine("then, Kirby!", 11, 13)

	textSequences.append(TextSequence("Lololo & Lalala", 100, 35))
	textSequences[9].addTextBox(TextBox("Lololo & Lalala 1", 0x1BD2E, 57, 20, 3, 6, 6, 21, 10))
	textSequences[9].textBoxes[0].addLine("To get this far you", 4, 7)
	textSequences[9].textBoxes[0].addLine("must have", 4, 9)
	textSequences[9].textBoxes[0].addLine("a-MAZE-ing skill", 4, 11)
	textSequences[9].textBoxes[0].addLine("Tee hee hee!!", 4, 13)
	textSequences[9].addTextBox(TextBox("Lololo & Lalala 2", 0x1BD8E, 43, 15, 11, 8, 6, 18, 8))
	textSequences[9].textBoxes[1].addLine("Oh yeah? Try and", 12, 9)
	textSequences[9].textBoxes[1].addLine("figure your way", 12, 11)
	textSequences[9].textBoxes[1].addLine("out of this!", 12, 13)

	textSequences.append(TextSequence("Bugzzy", 37, 15))
	textSequences[10].addTextBox(TextBox("Bugzzy 1", 0x1BDD7, 18, 5, 7, 10, 6, 20, 4))
	textSequences[10].textBoxes[0].addLine("ROOAAAAAAARRR!!!!!", 8, 11)
	textSequences[10].addTextBox(TextBox("Bugzzy 2", 0x1BDFD, 19, 10, 3, 10, 6, 15, 6))
	textSequences[10].textBoxes[1].addLine("Oh, I'm soooo", 4, 11)
	textSequences[10].textBoxes[1].addLine("scared", 4, 13)

	textSequences.append(TextSequence("Paint Roller", 174, 60))
	textSequences[11].addTextBox(TextBox("Paint Roller 1", 0x1BE27, 36, 10, 9, 10, 6, 20, 6))
	textSequences[11].textBoxes[0].addLine("Let me paint you a", 10, 11)
	textSequences[11].textBoxes[0].addLine("lovely portrait...", 10, 13)
	textSequences[11].addTextBox(TextBox("Paint Roller 2", 0x1BE62, 19, 10, 3, 10, 6, 15, 6))
	textSequences[11].textBoxes[1].addLine("Oh, how sweet", 4, 11)
	textSequences[11].textBoxes[1].addLine("of yo-", 4, 13)
	textSequences[11].addTextBox(TextBox("Paint Roller 3", 0x1BE8C, 33, 10, 10, 10, 6, 19, 6))
	textSequences[11].textBoxes[2].addLine("... of you losing", 11, 11)
	textSequences[11].textBoxes[2].addLine("to me, HA HA HA!", 11, 13)
	textSequences[11].addTextBox(TextBox("Paint Roller 4", 0x1BEC4, 57, 20, 3, 6, 6, 19, 10))
	textSequences[11].textBoxes[3].addLine("Paint Roller, you", 4, 7)
	textSequences[11].textBoxes[3].addLine("are the meanest", 4, 9)
	textSequences[11].textBoxes[3].addLine("art student I've", 4, 11)
	textSequences[11].textBoxes[3].addLine("ever met.", 4, 13)
	textSequences[11].addTextBox(TextBox("Paint Roller 5", 0x1BF22, 29, 10, 10, 10, 6, 19, 6))
	textSequences[11].textBoxes[4].addLine("Student? HA!", 11, 11)
	textSequences[11].textBoxes[4].addLine("I am the MASTER!!", 11, 13)

	textSequences.append(TextSequence("Heavy Mole", 130, 45))
	textSequences[12].addTextBox(TextBox("Heavy Mole 1", 0x1BF56, 59, 20, 11, 6, 6, 18, 10))
	textSequences[12].textBoxes[0].addLine("I am Heavy Mole,", 12, 7)
	textSequences[12].textBoxes[0].addLine("watch while I", 12, 9)
	textSequences[12].textBoxes[0].addLine("undermine your", 12, 11)
	textSequences[12].textBoxes[0].addLine("precious dream!!", 12, 13)
	textSequences[12].addTextBox(TextBox("Heavy Mole 2", 0x1BFB8, 71, 25, 3, 4, 6, 21, 12))
	textSequences[12].textBoxes[1].addLine("You are sneaky, but", 4, 5)
	textSequences[12].textBoxes[1].addLine("I will not be ", 4, 7)
	textSequences[12].textBoxes[1].addLine("distracted by your", 4, 9)
	textSequences[12].textBoxes[1].addLine("under-handed", 4, 11)
	textSequences[12].textBoxes[1].addLine("tactics.", 4, 13)

	textSequences.append(TextSequence("Mr. Shine & Mr. Bright", 152, 50))
	textSequences[13].addTextBox(TextBox("Mr. Shine & Mr. Bright 1", 0x1C02B, 34, 10, 9, 4, 6, 20, 6))
	textSequences[13].textBoxes[0].addLine("We rule both the", 10, 5)
	textSequences[13].textBoxes[0].addLine("night and the day!", 10, 7)
	textSequences[13].addTextBox(TextBox("Mr. Shine & Mr. Bright 2", 0x1C05F, 42, 15, 9, 3, 6, 20, 8))
	textSequences[13].textBoxes[1].addLine("This leaves no", 10, 4)
	textSequences[13].textBoxes[1].addLine("time for you", 10, 6)
	textSequences[13].textBoxes[1].addLine("Kirby! Be gone!!", 10, 8)
	textSequences[13].addTextBox(TextBox("Mr. Shine & Mr. Bright 3", 0x1C0A7, 76, 25, 1, 4, 6, 19, 12))
	textSequences[13].textBoxes[2].addLine("I thrive at dusk", 2, 5)
	textSequences[13].textBoxes[2].addLine("and at dawn!", 2, 7)
	textSequences[13].textBoxes[2].addLine("I'll have you two", 2, 9)
	textSequences[13].textBoxes[2].addLine("fighting before", 2, 11)
	textSequences[13].textBoxes[2].addLine("the day is done.", 2, 13)

	textSequences.append(TextSequence("Kracko", 114, 40))
	textSequences[14].addTextBox(TextBox("Kracko 1", 0x1C11F, 65, 20, 9, 2, 6, 20, 10))
	textSequences[14].textBoxes[0].addLine("KRRR-RACKK!!!!", 10, 3)
	textSequences[14].textBoxes[0].addLine("Dance to my deadly", 10, 5)
	textSequences[14].textBoxes[0].addLine("music, or fry like", 10, 7)
	textSequences[14].textBoxes[0].addLine("a moth! HA HA!!", 10, 9)
	textSequences[14].addTextBox(TextBox("Kracko 2", 0x1C187, 49, 20, 3, 6, 6, 21, 10))
	textSequences[14].textBoxes[1].addLine("You couldn't hit a", 4, 7)
	textSequences[14].textBoxes[1].addLine("barn sized", 4, 9)
	textSequences[14].textBoxes[1].addLine("lightning rod,", 4, 11)
	textSequences[14].textBoxes[1].addLine("Kracko!", 4, 13)

	textSequences.append(TextSequence("Meta Knight", 109, 40))
	textSequences[15].addTextBox(TextBox("Meta Knight 1", 0x1C1DF, 32, 10, 11, 8, 6, 18, 6))
	textSequences[15].textBoxes[0].addLine("None shall pass!", 12, 9)
	textSequences[15].textBoxes[0].addLine("En garde, Kirby!", 12, 11)
	textSequences[15].addTextBox(TextBox("Meta Knight 2", 0x1C216, 21, 10, 3, 10, 6, 15, 6))
	textSequences[15].textBoxes[1].addLine("But I have no", 4, 11)
	textSequences[15].textBoxes[1].addLine("sword!?!", 4, 13)
	textSequences[15].addTextBox(TextBox("Meta Knight 3", 0x1C242, 56, 20, 9, 4, 6, 20, 10))
	textSequences[15].textBoxes[2].addLine("Oh, you're so", 10, 5)
	textSequences[15].textBoxes[2].addLine("right...", 10, 7)
	textSequences[15].textBoxes[2].addLine("Then Avalanche it", 10, 9)
	textSequences[15].textBoxes[2].addLine("is, ha ha ha ha!!!", 10, 11)

	textSequences.append(TextSequence("King Dedede", 134, 40))
	textSequences[16].addTextBox(TextBox("King Dedede 1", 0x1C2A1, 54, 15, 8, 6, 6, 21, 8))
	textSequences[16].textBoxes[0].addLine("Kirby!! Your dream", 9, 7)
	textSequences[16].textBoxes[0].addLine("has carried you far", 9, 9)
	textSequences[16].textBoxes[0].addLine("but here it ends.", 9, 11)
	textSequences[16].addTextBox(TextBox("King Dedede 2", 0x1C2F0, 36, 10, 8, 6, 6, 21, 8))
	textSequences[16].textBoxes[1].addLine("The Dream Fountain", 9, 7)
	textSequences[16].textBoxes[1].addLine("Cup will be mine!!", 9, 9)
	textSequences[16].addTextBox(TextBox("King Dedede 3", 0x1C32B, 44, 15, 3, 8, 6, 18, 8))
	textSequences[16].textBoxes[2].addLine("Welcome King", 4, 9)
	textSequences[16].textBoxes[2].addLine("Dedede. And good", 4, 11)
	textSequences[16].textBoxes[2].addLine("luck to you too.", 4, 13)

def restoreOriginalTextToRom(verify=True):
	prepareOriginalTextSequences()
	writeTextSequencesToRom(verify, True)

def writeNewTextToRom(verify=True, textBoxConsistent=True):
	shutil.copy("D:\\Kirby's Avalanche - Rewritten\\Kirby's Avalanche (USA) - original\\Kirby's Avalanche (USA).sfc", "D:\\Kirby's Avalanche - Rewritten\\Kirby's Avalanche (USA).sfc")
	prepareNewTextSequences()
	writeTextSequencesToRom(verify, textBoxConsistent)

def writeTextSequencesToRom(verify=True, textBoxConsistent=True):
	global file

	if (not verify) or verifyAllTextSequences(textBoxConsistent):
		print("\nAll text sequences have been successfully verified.")
		for textSequence in textSequences:
			file = open(romFile, "rb")
			fileStart = file.read(textSequence.textBoxes[0].address) # unused
			textBoxEndings = []
			currAddress = textSequence.textBoxes[0].address
			for i in range(len(textSequence.textBoxes)):
				if i < (len(textSequence.textBoxes) - 1):
					textBox = textSequence.textBoxes[i]
					nextTextBox = textSequence.textBoxes[i+1]
					file.read(5)
					currAddress += 5
					file.read(textBox.numBytesNeeded)
					currAddress += textBox.numBytesNeeded
					textBoxEnding = file.read(nextTextBox.address - currAddress)
					textBoxEndings.append(textBoxEnding)
					currAddress += len(textBoxEnding)
			fileEnd = file.read(0xFFFFF - (textSequence.textBoxes[0].address + currAddress)) # unused
			file.close()
			file = open(romFile, "r+b")
			file.seek(textSequence.textBoxes[0].address)
			for i in range(len(textSequence.textBoxes)):
				textBox = textSequence.textBoxes[i]
				createNewTextBox(textBox.box_x, textBox.box_y, textBox.box_type, textBox.box_w, textBox.box_h)
				for line in textBox.lines:
					writeStringAtPos(line.text, line.x, line.y)
				if i < (len(textSequence.textBoxes) - 1):
					file.write(textBoxEndings[i])
			file.close()
		print("\nSUCCESS: Wrote text to rom.")
	else:
		print("\nFAILURE: At least one text box did not successfully verify.")

# address is the first letter from the text itself
def generateTextSequenceFromRom(name, addressesRounded):
	global textSequenceIndex, file

	textBoxArr = []
	bytesUsed_chars_total = 0
	bytesUsed_lines_total = 0
	for textBoxNum in range(len(addressesRounded)):
		addressRounded = addressesRounded[textBoxNum]
		file.seek(addressRounded)
		offset = 1
		while True:
			currChar = bytearray(file.read(1))[0]
			if currChar == 0:
				break
			offset += 1
		address = addressRounded + offset
		file.seek(address - 9)
		tb_info = bytearray(file.read(5)) # x, y, type, w, h
		bytesUsed_chars_textBox = 0
		bytesUsed_lines_textBox = 0
		lineStrArr = []
		while True:
			line_info = bytearray(file.read(4)) # text indicator, x, y, blank space
			if line_info[0] != 1:
				break
			text = ""
			while True:
				currChar = bytearray(file.read(1))[0]
				if currChar == 255:
					break
				if currChar == 0:
					text += ' '
				elif currChar == 27:
					text += '-'
				else:
					text += str(romToDecoded[chr(currChar)])
			bytesUsed_chars_textBox += len(text)
			bytesUsed_lines_textBox += 5
			lineStrArr.append("textSequences["+str(textSequenceIndex)+"].textBoxes["+str(textBoxNum)+"].addLine(\""+text+"\", "+str(line_info[1])+", "+str(line_info[2])+")")

		textBoxStr = "textSequences["+str(textSequenceIndex)+"].addTextBox(TextBox(\""+name+" "+str(textBoxNum+1)+"\", "+"0x"+hex(address - 9)[2:].upper()+", "+str(bytesUsed_chars_textBox)+", "+str(bytesUsed_lines_textBox)+", "+str(tb_info[0])+", "+str(tb_info[1])+", "+str(tb_info[2])+", "+str(tb_info[3])+", "+str(tb_info[4])+"))"
		textBoxArr.append([textBoxStr, lineStrArr])
		bytesUsed_chars_total += bytesUsed_chars_textBox
		bytesUsed_lines_total += bytesUsed_lines_textBox

	textSequenceStr = "textSequences.append(TextSequence(\""+name+"\", "+str(bytesUsed_chars_total)+", "+str(bytesUsed_lines_total)+"))"
	print('\t'+textSequenceStr)
	for textBox in textBoxArr:
		print('\t'+textBox[0])
		for line in textBox[1]:
			print('\t'+line)

	textSequenceIndex += 1
	print()

def generateTextSequencesFromRom():
	global file

	file = open(romFile, "r+b")
	generateTextSequenceFromRom("Waddle Dee",             (0x1B5C0, 0x1B5F0, 0x1B650))
	generateTextSequenceFromRom("Bronto Burt",            (0x1B680, 0x1B6C0, 0x1B710))
	generateTextSequenceFromRom("Waddle Doo",             (0x1B730, 0x1B7B0))
	generateTextSequenceFromRom("Dedede Intro",           (0x1B7D0, 0x1B850))
	generateTextSequenceFromRom("Poppy Bros. Sr.",        (0x1B8D0, 0x1B900, 0x1B970))
	generateTextSequenceFromRom("Whispy Woods",           (0x1B9D0, 0x1BA30))
	generateTextSequenceFromRom("Kabu",                   (0x1BA60, 0x1BAA0, 0x1BAE0))
	generateTextSequenceFromRom("Broom Hatter",           (0x1BB30, 0x1BB80, 0x1BBE0))
	generateTextSequenceFromRom("Squishy",                (0x1BC10, 0x1BC70, 0x1BCE0))
	generateTextSequenceFromRom("Lololo & Lalala",        (0x1BD30, 0x1BD90))
	generateTextSequenceFromRom("Bugzzy",                 (0x1BDD0, 0x1BE00))
	generateTextSequenceFromRom("Paint Roller",           (0x1BE20, 0x1BE60, 0x1BE90, 0x1BEC0, 0x1BF20))
	generateTextSequenceFromRom("Heavy Mole",             (0x1BF50, 0x1BFC0))
	generateTextSequenceFromRom("Mr. Shine & Mr. Bright", (0x1C030, 0x1C060, 0x1C0A0))
	generateTextSequenceFromRom("Kracko",                 (0x1C120, 0x1C180))
	generateTextSequenceFromRom("Meta Knight",            (0x1C1E0, 0x1C210, 0x1C240))
	generateTextSequenceFromRom("King Dedede",            (0x1C2A0, 0x1C2F0, 0x1C330))
	file.close()

def printRomText():
	file = open(romFile, "r+b")

	file.seek(startAddress)
	fbOriginal = bytearray(file.read(endAddress - startAddress + 1))

	counter = 0
	currAddress = startAddress
	for i in range(len(fbOriginal)):
		if currAddress%16 == 0:
			print("0x"+hex(currAddress)[2:].upper(), end='\t')
		if fbOriginal[i] == 0:
			newChar = ' '
		elif fbOriginal[i] == 27:
			newChar = '-'
		elif (chr(fbOriginal[i]) in romToDecoded.keys()):
			newChar = romToDecoded[chr(fbOriginal[i])]
		else:
			newChar = "<"+str(fbOriginal[i])+">"
			# print('*', end='')
		print(newChar, end='')
		if currAddress%16 == 15:
			print()
		currAddress += 1

	file.close()

def writeChar(c):
	if c == ' ':
		file.write(bytes([0]))
	elif c == '-':
		file.write(bytes([27]))
	else:
		file.write(bytes(decodedToRom[c], encoding='utf-8'))

def writeStringAtPos(s, x, y):
	file.write(bytes([1, x, y, 0]))
	for c in s:
		writeChar(c)
	file.write(bytes([255]))

def createNewTextBox(x, y, t, w, h):
	file.write(bytes([x, y, t, w, h]))

def keepOriginalTextBox():
	file.read(4)

def verifyAllTextSequences(textBoxConsistent=True):
	for textSequence in textSequences:
		if not textSequence.verify(textBoxConsistent):
			return False
	return True

class TextSequence:
	def __init__(self, name, numBytesUsed_chars, numBytesUsed_lines):
		self.name = name
		self.textBoxes = []
		self.numBytesNeeded = numBytesUsed_chars + numBytesUsed_lines

	def addTextBox(self, textBox):
		self.textBoxes.append(textBox)

	def verify(self, textBoxConsistent=True):
		numBytesUsed = 0
		for textBox in self.textBoxes:
			for line in textBox.lines:
				numBytesUsed += (5 + len(line.text))
		if numBytesUsed < self.numBytesNeeded and not textBoxConsistent:
			# print("\nNote: Too few bytes are used. Padding out the lowest line(s) with spaces.")
			# print("Recommended: "+str(self.numBytesNeeded))
			# print("Actual:      "+str(numBytesUsed))
			for j in range(len(self.textBoxes)-1, -1, -1):
				for i in range(len(self.textBoxes[j].lines)-1, -1, -1):
					while (numBytesUsed < self.numBytesNeeded) and ((len(self.textBoxes[j].lines[i].text) < self.textBoxes[j].maxTextLength) or (j == 0 and i == 0)):
						self.textBoxes[j].lines[i].text += " "
						numBytesUsed += 1
		if numBytesUsed > self.numBytesNeeded:
			print("\nERROR: Too many bytes are being used (1 per character, plus 5 per line).")
			print("Recommended: "+str(self.numBytesNeeded))
			print("Actual:      "+str(numBytesUsed))
			return False
		for textBox in self.textBoxes:
			if not textBox.verify(textBoxConsistent):
				return False
		return True

class TextBox:
	def __init__(self, name, address, numBytesUsed_chars, numBytesUsed_lines, box_x, box_y, box_type, box_w, box_h):
		self.name = name
		self.address = address
		self.numBytesNeeded = numBytesUsed_chars + numBytesUsed_lines
		self.box_x = box_x
		self.box_y = box_y
		self.box_type = box_type
		self.box_w = box_w
		self.box_h = box_h
		self.lines = []
		self.maxTextLength = math.floor(self.box_w * 16 / 17)
		self.maxNumLines = math.floor(self.box_h / 2.25)

	def addLine(self, text, x, y):
		self.lines.append(Line(text, x, y))

	def verify(self, textBoxConsistent=True):
		printedVerifyingMessage = False

		if textBoxConsistent:
			numBytesUsed = 0
			for line in self.lines:
				numBytesUsed += (5 + len(line.text))
			if numBytesUsed < self.numBytesNeeded:
				print("\nNote: Too few bytes are used. Padding out the lowest line(s) with spaces.")
				print("Recommended: "+str(self.numBytesNeeded))
				print("Actual:      "+str(numBytesUsed))
				for i in range(len(self.lines)-1, -1, -1):
					while (numBytesUsed < self.numBytesNeeded) and ((len(self.lines[i].text) < self.maxTextLength) or (i == 0)):
						self.lines[i].text += " "
						numBytesUsed += 1
			if numBytesUsed > self.numBytesNeeded:
				if not printedVerifyingMessage:
					print("\nVerifying Text Box \""+self.name+"\"...")
					printedVerifyingMessage = True
				print("ERROR: Too many bytes are being used (1 per character, plus 5 per line).")
				print("Recommended: "+str(self.numBytesNeeded))
				print("Actual:      "+str(numBytesUsed))
				return False

		for i in range(len(self.lines)):
			line = self.lines[i]
			if len(line.text) > self.maxTextLength:
				if not printedVerifyingMessage:
					print("\nVerifying Text Box \""+self.name+"\"...")
					printedVerifyingMessage = True
				print("Warning: Text length for line "+str(i+1)+" is longer than the recommended length for this box.")
				print("Recommended: "+str(self.maxTextLength))
				print("Actual:      "+str(len(line.text)))
		if len(self.lines) > self.maxNumLines:
			if not printedVerifyingMessage:
				print("\nVerifying Text Box \""+self.name+"\"...")
				printedVerifyingMessage = True
			print("Warning: Number of lines is longer than the recommended number of lines for this box.")
			print("Recommended: "+str(self.maxNumLines))
			print("Actual:      "+str(len(self.lines)))
		return True

class Line:
	def __init__(self, text, x, y):
		self.text = text
		if replaceAvalancheWithPuyo:
			self.text = self.text.replace("Avalanche", "Puyo Puyo")
		self.x = x
		self.y = y

def main():
	global replaceAvalancheWithPuyo

	verifyRomIntegrity()
	print("Valid rom detected. If you would like to continue and replace the game's text as defined in the text editor, type \"Go\" (without quotation marks). Otherwise, close the program.")
	print("WARNING: This will replace the current rom. Back it up if you haven't already!")
	choice = input()
	if choice != "Go":
		sys.exit()
	if len(sys.argv) > 1:
		if sys.argv[1] == "--print":
			printRomText()
		elif sys.argv[1] == "--puyo":
			print("Generating Puyo version...")
			replaceAvalancheWithPuyo = True
			writeNewTextToRom(verify=True, textBoxConsistent=True)
		elif sys.argv[1] == "--normal":
			print("Generating normal version...")
			replaceAvalancheWithPuyo = False
			writeNewTextToRom(verify=True, textBoxConsistent=True)
		else:
			print("Invalid argument(s).")
	else:
		if replaceAvalancheWithPuyo:
			print("Generating Puyo version...")
		else:
			print("Generating normal version...")
		writeNewTextToRom(verify=True, textBoxConsistent=True)
		# restoreOriginalTextToRom()
		# generateTextSequencesFromRom()

if __name__ == "__main__":
	main()
