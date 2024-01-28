# SHOW-MY-ANSWERS

**This repository contains a Python script that automatically fetches answers for CISCO NetAcad Courses exams.**

## How to Use

### Prerequisites
- Install necessary modules using pip.
- Website to convert JS Object to JSON: [ConvertSimple](https://www.convertsimple.com/convert-javascript-to-json/)

### Steps
1. Open the Exam Window and press Ctrl + U (for Mac, use Command+U).
   <img src="https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/2674b2ec-2c29-4fc5-a1e5-6c23484ca2e4" width="500" height="300"><br>

2. A new window will open, displaying the exam page source code.

3. Scroll to the bottom of the page, where you'll find a script tag containing a JavaScript variable called 'data' (e.g., `let data = {...}`).
   <img src="https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/b0e12a5b-dca1-4ff2-908a-1f0f210417d1" width="500" height="300"><br>

4. Copy the contents inside that script tag.

5. Open [ConvertSimple](https://www.convertsimple.com/convert-javascript-to-json/) and paste the copied JavaScript code.

6. It may show that the code is invalid; remove the last line of that code, i.e., `Object.freeze(data);`.

7. You'll get the respective JSON Object; copy that code.
   <img src="https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/31cfbbce-ece0-4a10-a4d6-6c0f8a5211b9" width="500" height="300"><br>

8. Download the Python script provided in this repository.

9. Create a new folder, put the script in a separate folder, and create a new file called 'data.json.' Paste the JSON code into this file.
   <img src="https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/599f66aa-941c-4e11-9317-15b01218bae8" width="500" height="300"><br>
   <img src="https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/7edef3d7-6fb3-460b-bc55-59ca55803fa9" width="500" height="300">

10. Run the Python script.
    <img src="https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/74d8f9ec-06d0-4cf8-b53b-3ba737b705b0" width="500" height="300"><br>

## Note
- Sometimes, this script fails to provide correct answers/options. If you notice this, restart the exam and repeat the above steps.
- This script works fine for multiple choices, but be careful while selecting options!

## Disclaimer
Use this script/program for educational purposes only. I am not responsible for any misuse of this tool.
