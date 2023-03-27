<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Kush Sudhir Borikar (kb97)</td></tr>
<tr><td> <em>Generated: </em> 3/27/2023 7:13:01 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/kb97" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227947714-7c0a976f-4ee1-4f38-85c3-5f49af7f243e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code that calculates the cost of all<br>the in-progress burger array, sums it up and returns it.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>I first initialized a variable that will hold the cost of the burger<br>(in-progress), then run a for loop over the array &quot;inprogress_burger&quot;, and for every<br>item in this array, the variable cost of burger will be incremented by<br>the value of the corresponding item. Once the array is complete, the cost<br>of burger will be returned.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227949539-c1dfbd00-d1a6-46f4-8cad-6c8c8487effe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This snippet of code shows how the out of stock exception is handled,<br>I have created the outofstock exception as an event and trigger it when<br>any item is out of stock and display appropriate message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227953162-7bf98031-4b98-446d-a4fa-b6e1649b4bc3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This snippet of code shows how after 15 (defined by default) uses of<br>the machine, the user is prompted to to clean the machine by entering<br>an input, if the input is entered correctly, the machine is cleaned and<br>a message showing success is printed, if not, a message showing failure to<br>clean the machine is printed. This is also shown in the output.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227954711-b0ea5295-e63f-4a94-8b66-96a853a9dec1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This snippet of code shows how the invalid choice exception has been handled,<br>if the user enters any input that does not correspond to the value<br>in that particular stage, for example, if the machine is prompting the user<br>for a patty and the users enters a bun or topping, this will<br>be displayed as an invalid choice. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227955922-34b641ce-e47c-44ef-81b2-efac9a87b3b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This snippet of code shows if a user exceeds the number of choices<br>made in a particular stage, since we have defined that number of toppings<br>and patty cannot exceed 3 choices, this exception will be thrown and the<br>users will be displayed with a message that they have exceeded the number<br>of choices permitted in the particular stage.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227951394-38837300-8b3a-4c85-9d4d-c4d90a2257c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This snippet of code shows how the invalidpayment is handled, if the users<br>does not input the exact amount as displayed by the burger machine, it<br>will be prompted as an invalid payment method and asked to try again,<br>the screenshot also shows this in the output.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Out of Stock Exception - For patties and toppings, their stock is<br>of 10 items each, once these items are out of stock, and the<br>user tries to use the out of stock item in his/her burger, they<br>will be displayed with a message, that the item is out of stock.<br><br>2.<br>Needs Cleaning Exception - We have defined the uses of machine until cleaning<br>as 15, so once 15 uses of machines are performed, it will prompt<br>the user to enter the expression &#39;clean&#39; to clean the machine, successful cleaning<br>will display a message of success and failure will show the corresponding message.<div><br></div><div>3.<br>Invalid Choice Exception - If a user tries to enter an input which<br>does not correspond to the respective stage the machine is in, this exception<br>will display a message that shows that this is an invalid choice.</div><div><br></div><div>4. Exceeded<br>Remaining Choices Exception -&nbsp; Since we have defined that number of toppings and<br>patty cannot exceed 3 choices, this exception will be thrown and the users<br>will be displayed with a message that they have exceeded the number of<br>choices permitted in the particular stage.</div><div><br></div><div>5. Invalid Payment Exception -&nbsp; If the users<br>does not input the exact amount as displayed by the burger machine as<br>the cost of the burger, it will be prompted as an invalid payment<br>and asked to try again. Once the exact amount is entered, the machine<br>will display the payment as successful.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227990145-29a8488e-0c84-44a9-a866-42f0dbb225f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code of the 1st test case that<br>checks for an Invalid Stage exception.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227990472-905a7bc4-86b2-4875-bcfd-5dcf685a6637.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code of the 2nd test case that<br>checks if a patty is in stock or not, and also if an<br>exception is triggered in the event of out of stock.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227991778-a359d4b2-b0cb-464a-92af-38b0137750ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code of the 3rd test case that<br>checks if a topping is in stock or not, and also if an<br>exception is triggered in the event of out of stock.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227993360-8cb0b93f-9232-42c9-a3ad-cf770dc20ce3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code of the 4th test case that<br>checks that not more than a combination of 3 patties can be added<br>to a burger and also if an exception is triggered in the event<br>of exceeded remaining choices<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227995226-02a2e7e4-e72c-4719-969d-04c8378007f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code of the 5th test case that<br>checks that not more than a combination of 3 toppings can be added<br>to a burger and also if an exception is triggered in the event<br>of exceeded remaining choices<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227997658-4449fb22-825b-463b-b4b8-03382e89ead9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code of the 6th test case that<br>checks the cost of burger for some random burgers that, it checks if<br>the costs of these random burgers come out to be the same as<br>the cost of actual burgers.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227999899-5439d6d6-a790-492d-ac05-fc460e7ee3e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code of the 7th test case that<br>checks the total sales of any 2-3 burgers, and compares it&#39;s projected cost<br>to it&#39;s actual cost.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/228000114-9730226d-d567-4296-86fd-3fc7fe147d8a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code of the 8th test case that<br>checks the total number of burgers made, it is checking if the expected<br>total burgers and the machine total burgers match to see if burgers are<br>incrementing after each purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/228000579-b2689f3f-2a4d-42ac-b720-c1a76bb88885.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tests 1-8 passing and relevant output <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test Case 1 -&nbsp; Checks for an Invalid Stage exception.<br><br>Test Case 2 -&nbsp;<br>Checks if a patty is in stock or not, and also if an<br>exception is triggered in the event of out of stock.<br><div><br></div><div>Test Case 3 -<br>Checks if a topping is in stock or not, and also if an<br>exception is triggered in the event of out of stock.<br></div><div><br></div><div>Test Case 4 -<br>Checks that not more than a combination of 3 patties can be added<br>to a burger and also if an exception is triggered in the event<br>of exceeded remaining choices<br></div><div><br></div><div>Test Case 5 -&nbsp; Checks that not more than a<br>combination of 3 toppings can be added to a burger and also if<br>an exception is triggered in the event of exceeded remaining choices<br></div><div><br></div><div>Test Case 6<br>- Checks the cost of burger for some random burgers that, it checks<br>if the costs of these random burgers come out to be the same<br>as the cost of actual burgers.<br></div><div><br></div><div>Test Case 7 - Checks the total sales<br>of any 2-3 burgers, and compares it&#39;s projected cost to it&#39;s actual cost.<br></div><div><br></div><div>Test<br>Case 8 -&nbsp; Checks the total number of burgers made, it is checking<br>if the expected total burgers and the machine total burgers match to see<br>if burgers are incrementing after each purchase</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/14">https://github.com/kush0698/IS601-004/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>I was not able to figure out the currency format for the cost_of_burger.<br>I learned about handling and creating exceptions and learned in detail about test<br>cases from this particular mini project.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/227962541-44fcdda2-e8f9-4bc8-b890-cbea5c8c754c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the output of the burger machine for a few different<br>combination of burgers.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/kb97" target="_blank">Grading</a></td></tr></table>