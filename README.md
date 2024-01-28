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
    <li>A new Window will be opened and you can see exam page source code</li>
    <li>go very bottom of that page where you'll find a script tag conatins a js variable called 'data' i.e let data = {...}</li>
    <li>copy that line (contents inside that scipt tag).</li>
    <li>goto [this](https://www.convertsimple.com/convert-javascript-to-json/) website.</li>
    <li>paste the JS object/thing that you have copied.</li>
    <li>it shows code is invalid - remove last of that code i.e Object.Freeze(data);</li>
    <li>you'll get respective JSON Object, copy that code.</li>
    <li>Download the Python script provided in this this repo.</li>
    <li>create a new folder and put this script in a separate folder, and create a new file called 'data.json' and paste the JSON code.</li>
    <li>that's all, run the python script.</li>
  </ul>
</p>
# Disclaimer
<h3>Use this Script/Program for Educational Purposes, i'm not at all responsible for any missuse of this thing...</h3><br>
