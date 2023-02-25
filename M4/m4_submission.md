<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Kush Sudhir Borikar (kb97)</td></tr>
<tr><td> <em>Generated: </em> 2/25/2023 2:20:59 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/kb97" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221304835-10ae9eeb-52fa-4cb8-bd87-862c5ec89f86.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that shows the addition function and the<br>output of a valid addition operation.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221305020-2067e880-a5b8-4090-9945-fb360b05967a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that shows the subtraction function and the<br>output of a valid subtraction operation.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221305266-9d6972f8-35b0-4c01-b370-f0d490fa71fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that shows the multiplication function and the<br>output of a valid multiplication operation.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221306332-5ffb5eb3-11e1-4a00-977b-2eee0de26517.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that shows the division function and the<br>output of a valid division operation and handling division by zero as well.<br><br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221308562-69a7e85a-8e8c-46ef-9fad-4c5a13301f65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that is a test case function for<br>the addition operation of two normal operands.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221309227-1e111135-b22a-47ab-83c6-27c16d302b26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that is a test case function for<br>the addition operation of &quot;ans&quot; and a normal operand, and of &quot;ans&quot; as<br>both operands as well.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221310014-39da8b6b-91fd-4b95-9bac-d07026a315e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that is a test case function for<br>the subtraction operation of two normal operands.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221317317-32b22170-ec6a-4c52-8589-325b7200bfc3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that is a test case function for<br>the subtraction operation of &quot;ans&quot; and a normal operand, and of &quot;ans&quot; as<br>both operands as well.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221318086-e6a9ddbe-641d-44c4-bef3-2c23e68cd71b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that is a test case function for<br>the multiplication operation of two normal operands.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221318653-74da10ef-b6ee-499e-b51c-c7f441ccafb8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that is a test case function for<br>the multiplication operation of &quot;ans&quot; and a normal operand, and of &quot;ans&quot; as<br>both operands as well.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221318849-ebbc64af-a205-4ef8-a607-6775f340e9a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that is a test case function for<br>the division operation of two normal operands.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/221319021-0ff48d47-6acf-4608-b18f-3528904b8482.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the snippet of code that is a test case function for<br>the division operation of &quot;ans&quot; and a normal operand, and of &quot;ans&quot; as<br>both operands as well.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I have learned about classes and objects. How to create functions. And also<br>how to pass arguments to a class and it&#39;s functions.&nbsp;&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Learned about the pytest library,&nbsp; how to use the assert keyword to run<br>test cases. Various values are passed to each test case function and is<br>checked for expected output. If all the assertions are passed, the test cases<br>are passed. I have created 10 test cases for the MyCalc.py file. This<br>handles the required test cases mentioned above as well as division by zero<br>error if it exists.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/compare/dev...M4-Simple-Calc?expand=1">https://github.com/kush0698/IS601-004/compare/dev...M4-Simple-Calc?expand=1</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/kb97" target="_blank">Grading</a></td></tr></table>