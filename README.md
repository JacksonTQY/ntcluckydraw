# How to use the NTC Lucky Draws
The lucky draw codes are for the purposes of the National Tax Competition only. 

There are 2 types of lucky draw codes that you can use (ntcchoose.py and GUI.py) but only one is needed. It is up to you which one you prefer to use. Both types assume the following:

*	The list of NTC participants is saved in a csv file called NTC_Participants.csv. There is a header row in the csv file and only 1 column containing the names of participants. Each participant is in a new row.
*	There are 10 consolation prize winners, a 3rd place winner, a 2nd place winner and a 1st place winner
*	Winners cannot win more than one prize so they are removed from the lucky draw pool
*	For 3rd, 2nd and 1st place winners, if the winner is not present, there will be a re-draw to get a new winner.
*	For consolation prize winners, it does not matter if the winner is present. Consolation prizes will only be drawn once and all consolation prize winners are drawn at the same time.

It is important to test the codes before the actual day for any bugs or errors.
### 1. ntcchoose.py
This is a normal python script file. 

<b>What you need: </b>
*	The Python script file (ntcchoose.py)
*	Python 3 installed on your computer
*	A csv file containing the list of the NTC participants’ names (NTC_Participants.csv)

The py file and csv file should be in the same folder/directory.

<b>How to use?</b>

Just run the file like you would run a normal python file. When prompted to move on to the next prize, enter “y” (if the prize winner is present) or “n” (if the prize winner is not present; this essentially generates a new random winner for that prize).
 ![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/921d02b1-237f-4a28-8df6-b9cdecc3a3b6)

Note:
1) 	Depending on which software you use to open the python file, you may get an error message about unrecognised modules similar to below:

 ![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/46be6162-48f6-4f19-a596-818dd3b6d782)

In such cases, you can either: a) install the relevant modules (Google for more information on how to do so), b) use a different IDE/software that has the modules pre-installed such as Anaconda, or c) run the file without python, such as via py2exe (Google for more information).

2)	If the file is not a csv file but an Excel file, please save it in a csv format with the name NTC_Participants.csv
3)	Depending on which version you have, the script may not actually be reading from the csv file containing the participants. If so, make the necessary changes to read from a csv file (example as shown, but not the only method):

![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/036d5b49-cd47-4f4a-8019-3016157323c7)

4)	If your file has print(consolation) remove that line.

  ![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/8d0f7d79-0ef7-4f63-bf06-72d10245c5ac)

6)	 exit() may not work properly for some. You may consider importing sys and replacing exit() with sys.exit()
 
 
### 2. GUI.py
This is a fancier GUI version of the lucky draw. It is more user-friendly and aesthetic but also harder to edit the source code.

<b>What you need: </b>
* The python script file (GUI.py)
*	Python 3 installed on your computer
* A csv file containing the list of the NTC participants’ names (NTC_Participants.csv)
*	An image of the NTC logo without the year (ntclogonoyear.png)

The py file, csv file and logo should be in the same folder/directory. By default, the logo and py file should already be in the same folder. In the event it isn’t, you may use this as a placeholder:

 ![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/7bad30db-ef3c-4cbb-ad7a-6157c8f86f4c)

<b>How to use?</b>

To use this version, just run the file like you would run a normal python file. A popup should appear as shown (may look different for different computers, especially Mac)

 ![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/1cb0cefb-80a5-4d64-9245-8ef065f7f728)

When you see this home screen, click on “Generate lucky draw winners”.  A pop-up will appear with the list of the consolation prize winners. Once they have been noted, close the pop-up. The program will prompt you to click on “Claimed!” to move on to the 3rd place prize. 

  ![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/a251899c-1c57-49b8-a797-c64b14e16f1d)![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/864a241e-5180-4e4d-b2df-33de95c111c7)

![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/f9aa471e-37f0-4193-9c2d-b4a30fd887e9)![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/8082a6a6-7aef-4fc6-819b-b1c6d9da84c9)


The program will prompt you to click “Generate”. Click on it and wait to get a lucky draw winner for the 3rd prize. The lucky draw winner will be the name that appears in red. <b>If the person is present, click on “Claimed!” to move on to the next prize. If the person is not present, click on “Generate” to re-generate a new winner.</b> This is important as if you click “Claimed” by accident, you cannot go back and there will be no winner for this prize.

The above also applies for 2nd and 1st prize.

The list of names will be saved to a csv file for cross-checking purposes. If necessary, you may pass this file to the Financial Controller. Regardless, this file should be deleted once the prizes have been distributed due to PDPA reasons.

Note:
1)	Depending on which software you use to open the python file, you may get an error message about unrecognised modules similar to below:

 ![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/25e4f1d3-61d6-4b35-baba-6a3d1255fb62)

In such cases, you can either: a) install the relevant modules (Google for more information on how to do so), b) use a different IDE/software that has the modules pre-installed such as Anaconda, or c) run the file without python, such as via py2exe (Google for more information).

2)	Do not change the year. The year reflects the current year, so it will be correct on the actual day. The year and logo have been made such that it does not need to be updated.
3)	However, if the logo design for the year changes significantly, insert the new image into the folder and replace “ntclogonoyear.png” with the name of the new image (with quotation marks). Resize the image to be 500x300px or change the width and height if necessary.

 ![image](https://github.com/JacksonTQY/ntcluckydraw/assets/97141507/9bc53212-660a-483b-a847-1ab36ddc1696)

4)	If the input file is not a csv file but an Excel file, please save it in a csv format with the name NTC_Participants.csv
5) The winners will be saved as “Lucky Draw Winners.csv”. Do not open the file when the program is running as this will prevent you from saving the winners into the file.
6)	Avoid resizing the program window.

