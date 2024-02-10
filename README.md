# SHOW-MY-ANSWERS!

**This tool is a Python script meticulously crafted to simplify the often tedious task of gathering answers for CISCO NetAcad Course exams. By following a series of straightforward steps, users can effortlessly extract exam data from the source code and swiftly obtain accurate answers using the script. This automation significantly reduces the time and effort required for exam preparation, allowing users to focus more on understanding concepts rather than searching for answers. It serves as a valuable resource for learners seeking to optimize their study process and achieve better academic outcomes in CISCO NetAcad courses.**

## How to Use?

### Prerequisites
- Install `bs4` module using pip. Command: `pip install bs4` or `pip3 install bs4` or `python -m pip install bs4`.
- Website to convert JS Object to JSON: [ConvertSimple](https://www.convertsimple.com/convert-javascript-to-json/)

### Steps

1. Open the Exam Window and press `Ctrl + U`. for Mac, use `Option+Command+U`.<br><br>
   ![Step 1](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/2674b2ec-2c29-4fc5-a1e5-6c23484ca2e4)

2. A new window will open, displaying the exam page source code.

3. Scroll to the bottom of the page, where you'll find a script tag containing a JavaScript variable called `data` (i.e., `let data = {...}`).<br><br>
   ![Step 3](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/b0e12a5b-dca1-4ff2-908a-1f0f210417d1)

4. Copy the contents inside that script tag.

5. Open [ConvertSimple](https://www.convertsimple.com/convert-javascript-to-json/) and paste the copied JavaScript code.

6. It may show that the code is invalid; remove the last line of that code, i.e., `Object.freeze(data);`.<br><br>
   ![3](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/78d1c429-d00f-42ef-afcb-1d73705820f0)

8. You'll get the respective JSON Object; copy that code and Create a new folder then create a new file in that folder called 'data.json' and Paste the JSON code into this file<br><br>
   ![Step 7](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/31cfbbce-ece0-4a10-a4d6-6c0f8a5211b9)<br>
   ![Step 9](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/599f66aa-941c-4e11-9317-15b01218bae8)

10. Now, Download the [Python Script](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/blob/main/main.py) provided in this repository. put the script in same folder where you have already cteated `data.json`.<br><br>
   ![Step 9](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/7edef3d7-6fb3-460b-bc55-59ca55803fa9)

12. Run the Python script, That's all. [**MAKE SURE TO KEEP BOTH FILES IN SAME FOLDER AND MAKE SURE THAT YOU HAVE INSTALLED NECESSARY PYTHON PACKAGES MENTIONED ABOVE.**]<br><br>
    ![Step 10](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/74d8f9ec-06d0-4cf8-b53b-3ba737b705b0)
13. You need to repeat the above steps for all exams.
## Note ~

- Sometimes, this script fails to provide correct answers/options. If you notice this, restart the exam and repeat the above steps.
- This script works fine for multiple choices(where you have to choose <=2 options), but please exercise caution when selecting options for questions with more than 2 choices!

## Disclaimer!

**Use this script/program for educational purposes only. I am not responsible for any misuse of this tool. By utilizing this script, you acknowledge that any misuse or unethical use of the provided software is strictly your own responsibility. Always adhere to ethical standards and respect the rules and guidelines set by educational institutions.**
