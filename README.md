# SHOW-ANSWERS

**This repository contains a python script that will automatically fetch answers for any CISCO NetAcad Courses exams**
<br/>
<h2>How to Use!</h2>
<h4>Before that</h4>
<pre>
Notes:
- install necessary modules using pip
- website to convert JS Object to JSON: https://www.convertsimple.com/convert-javascript-to-json/
</pre>
<p>
  <h4>Steps</h4>
  <ul>
    <li>Open Exam Window and Press Ctrl + U (if Mac Command+U)</li>
    ![1](https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/2674b2ec-2c29-4fc5-a1e5-6c23484ca2e4)
    <li>A new Window will be opened and you can see exam page source code</li>
    <li>go very bottom of that page where you'll find a script tag conatins a js variable called 'data' i.e let data = {...}</li>
    ![2](https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/b0e12a5b-dca1-4ff2-908a-1f0f210417d1)
    <li>copy that line (contents inside that scipt tag).</li>
    <li>goto ![this](https://www.convertsimple.com/convert-javascript-to-json/) website and paste the JS code that you copied.</li>
    <li>it shows code is invalid - remove last of that code i.e Object.Freeze(data);</li>
    ![3](https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/500f98ad-4af3-48fd-ae3d-ea253e6efeb0)
    <li>you'll get respective JSON Object, copy that code.</li>
    ![4](https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/8996a1a3-8d15-447f-80f2-cb81d1aac1ae)
    <li>Download the Python script provided in this this repo.</li>
    <li>create a new folder and put this script in a separate folder, and create a new file called 'data.json' and paste the JSON code.</li>
    ![5](https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/599f66aa-941c-4e11-9317-15b01218bae8)
    ![6](https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/7edef3d7-6fb3-460b-bc55-59ca55803fa9)
    <li>that's all, run the python script.</li>
    ![7](https://github.com/PavanTheHacker55/SHOW-ANSWERS/assets/71021764/40660acf-03f7-46dc-9389-24a1565025aa)
  </ul>
</p>
# Disclaimer
<h3>Use this Script/Program for Educational Purposes, i'm not at all responsible for any missuse of this thing...</h3><br>
