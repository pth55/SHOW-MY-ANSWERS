## SHOW-MY-ANSWERS!

*This tool is a Python script meticulously crafted to simplify the often tedious task of gathering answers for CISCO NetAcad Course exams. By following a series of straightforward steps, users can effortlessly extract exam data from the source code and swiftly obtain accurate answers using the script. This automation significantly reduces the time and effort required for exam preparation, allowing users to focus more on understanding concepts rather than searching for answers. It serves as a valuable resource for learners seeking to optimize their study process and achieve better academic outcomes in CISCO NetAcad courses.*

## How to Use?

### Prerequisites
- Website to convert JS Object to JSON: [ConvertSimple](https://www.convertsimple.com/convert-javascript-to-json/)

### Steps

1. Open the Exam Window and press `Ctrl + U`. For Mac, use `Option+Command+U`.<br><br>
   ![Step 1](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/2674b2ec-2c29-4fc5-a1e5-6c23484ca2e4)

2. A new window will open, displaying the exam page source code.

3. Scroll to the bottom of the page, where you'll find a script tag containing a JavaScript variable called `data` (i.e., `let data = {...}`).<br><br>
   ![Step 3](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/b0e12a5b-dca1-4ff2-908a-1f0f210417d1)

4. Copy the contents inside that script tag.

5. Open [ConvertSimple](https://www.convertsimple.com/convert-javascript-to-json/) and paste the copied JavaScript code.

6. It may show that the code is invalid; remove the last line of that code, i.e., `Object.freeze(data);`.<br><br>
   ![Step 6](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/78d1c429-d00f-42ef-afcb-1d73705820f0)

7. You'll get the respective JSON Object, Copy that code.<br><br>
   ![Step 7](https://github.com/PavanTheHacker55/SHOW-MY-ANSWERS/assets/71021764/31cfbbce-ece0-4a10-a4d6-6c0f8a5211b9)

8. Now Download the Tool/Software from [HERE!](https://github.com/pth55/SHOW-MY-ANSWERS/releases/download/v2/show_my_answers.exe)

9. Now just Double click that executable to open the actual software.<br>

10. Here you need to do 3 things:
    - Paste the JSON code that you have copied in step 7 into that textarea.
    - Click on "SAVE JSON" button.
    - Click on "GET ANSWERS" to get the answers window.<br><br>
    ![Step 9](https://github.com/pth55/SHOW-MY-ANSWERS/assets/71021764/e5616e06-cb11-4ec7-bbc0-496268add151)

11. Now the answers window will be opened separately.<br><br>
    ![Step 11](https://github.com/pth55/SHOW-MY-ANSWERS/assets/71021764/e73fdce0-a5e4-4de4-afd7-1b58b9c79e94)

12. That's all! Write your exam and click "CLOSE" button to get back to the home/main window to write the next exam.

## Note

- Sometimes, this script fails to provide correct answers/options. If you notice this, restart the exam and repeat the above steps.
- This script works fine for multiple choices (where you have to choose <=2 options), but please exercise caution when selecting options for questions with more than 2 choices!

## Disclaimer

*Use this script/software for educational purposes only. I am not responsible for any misuse of this tool. By utilizing this script, you acknowledge that any misuse or unethical use of the provided software is strictly your own responsibility. Always adhere to ethical standards and respect the rules and guidelines set by educational institutions.*
