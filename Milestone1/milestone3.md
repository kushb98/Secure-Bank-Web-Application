<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Kush Sudhir Borikar (kb97)</td></tr>
<tr><td> <em>Generated: </em> 5/2/2023 2:05:03 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/kb97" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235544048-9987e318-6e6d-40fd-a3cc-e2861a40167c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows page showing heading as Internal Transfer and Heroku dev URL visible.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235546870-dcb372dd-9c03-42cb-b74c-c35345ce3616.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website that shows a successful internal tranfer.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235544190-b23d417e-0441-4f09-a71a-133e21497fcd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing dropdown values as requested of account source.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235544281-474ff5f8-b5f6-4206-8d38-89d986d1067f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing dropdown values as requested of account destination.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235544631-07add01b-2fb9-4539-8e74-d52a37dd2720.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows flash message that is showing transferring more funds than balance is<br>not possible.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235544815-4d78a55a-8ec5-4538-9c9e-7fcedf1afae5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows website shows proper flash message when user tries to transfer between<br>same accounts.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235545217-f922f077-bcde-433a-a9fc-840acb87cdbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows snippet of  code that prevents this functionality on the server<br>side.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235545345-7083e24c-2ca6-4e8e-9947-14b240326fc8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website that validates negative funds entry and shows proper message to<br>prevent it.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235545561-9621d5ee-00e1-4b45-b3f6-1220567ea6d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows snippet of  code that prevents entering funds value as negative<br>value.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235545908-890e9825-836f-4779-b861-ab455a74dacb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB showing the internal transfer transactions highlighted in the table. (Walmart<br>Bill Transfer)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235546054-1812473a-1616-4db9-86be-32156000d1fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB showing the account balance of account 000000000005 that matches the<br>expected total, so my code logic works properly.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <div>1) Using the user ID fetched from session data, a select query retrieves<br>all accounts associated with the current logged-in user. The resulting list of accounts<br>is then passed to the Jinja template for the transfer money page, where<br>each account is iterated over to create dropdown options.</div><div>2) Two separate select queries<br>fetch the balances of the source and destination accounts, respectively. If the source<br>account balance is insufficient to cover the transfer amount or the destination account<br>does not exist or is the same as the source account, an appropriate<br>error message is displayed. Two update queries are then executed, one to subtract<br>the transfer amount from the source account balance, and the other to add<br>it to the destination account balance. Once both queries are successful, a new<br>record is inserted into the transactions table, which includes details such as the<br>source and destination account numbers, the transfer amount, and other relevant information.</div><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/37">https://github.com/kush0698/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/accounts/transfer">https://is601-kb97-prod.herokuapp.com/accounts/transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235551527-73d2ad0b-50ee-4d18-b52f-8a071aac2f76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows list of transactions of transfer as highlighted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235549202-7e17a7a6-afb2-49d7-a530-56cf02f34b93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot demonstrating the use of deposit filter in transaction type and relevant result.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235549594-3e822bf3-71ce-4c30-a654-c40642264113.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot demonstrating the use of withdraw filter in transaction type and relevant result.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235551635-a4be73aa-7722-4847-a477-161892f8de21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot demonstrating the use of transfer filter in transaction type and relevant result.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235551696-d9eec14f-7632-4735-9e1e-44f700271e57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows pagination in our website page if an account has more than<br>10 transactions.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <div>To enable pagination, the website sets the number of items to be displayed<br>per page. This value is passed to the 'rows' variable, which determines the<br>number of rows to be shown on the page.&nbsp;</div><div><br></div><div>As for filtering, a variable<br>named 'transaction type' is used to store the input from the user. This<br>input is obtained through the 'request.args' function, which searches for the specified argument<br>in the table and displays the relevant data based on the filters applied.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/39">https://github.com/kush0698/IS601-004/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/accounts/transactions">https://is601-kb97-prod.herokuapp.com/accounts/transactions</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235577501-bd23b49c-e786-499d-a35f-e6bf6de2e790.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the user&#39;s profile with the new fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235577707-6a935121-8f50-4295-95c5-858fe0af8f91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing DB of users table and highlighted the entry in users table,<br>so that it can be verified that correct data is pulled in profile<br>page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/40">https://github.com/kush0698/IS601-004/pull/40</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/profile">https://is601-kb97-prod.herokuapp.com/profile</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235586055-90586d34-a04d-4195-ad03-544fc2712e1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the external transfer page with filled in data.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235586261-9a4fb0b4-c51a-4ca3-938e-15c9ee2c093f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing user can&#39;t send more than they have<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235586706-096b70f1-2237-4021-8810-2269c4116693.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows snippet that prevents user from sending more than they have.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235586921-98a3f521-5ada-47f3-99eb-78049b85b1c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing user can&#39;t send a negative amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235587036-bd3b9f4f-1ef1-45e3-b977-38764eba68cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the code snippet that prevents user from sending a negative amount.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235587619-a0fc4e65-398e-452d-9185-eb0bf34baee3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows user is not found if incorrect information is entered.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235587871-98025859-1707-4a81-80a3-6a89a8657713.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing snipper of code that prevents transfer to a account or user<br>that is not found.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235588127-3f51a9bc-9733-4efd-9a2a-75f135e5d5f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows Transaction table that shows transaction from ID 67 to 74 as<br>external transfers as highlighted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235589150-6c73d7f6-7737-447b-89b0-4e66f425ada3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the updated account balances, which can be verified from expected total<br>columns of the transaction tables.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <div>The transfer function begins by executing a select query, which searches for the<br>destination account entered by the user. The account number is verified by comparing<br>the last 4 digits of the account number in the accounts table with<br>the last 4 digits of the account number entered by the user. Additionally,<br>the last name is verified by searching the users table.</div><div><br></div><div>If the select query<br>returns a match, the transfer is initiated. However, if the select query fails<br>to return a match, the appropriate error message is displayed to the user.</div><div><br></div><div>This<br>approach ensures that the transfer is made only to a valid account and<br>the user has entered the correct account details. It also prevents the transfer<br>of funds to an account that does not exist.</div><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/42">https://github.com/kush0698/IS601-004/pull/42</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/accounts/ext_transfer">https://is601-kb97-prod.herokuapp.com/accounts/ext_transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Here are some possible rephrased and expanded versions:</div><div><br></div><div>1. One of the skills I<br>acquired was the ability to transfer data between web pages either through arguments<br>or by using session data. This allows for the passing of critical information<br>between different parts of the website and enables users to carry out specific<br>actions based on the information they provide.</div><div><br></div><div>2. Another skill I learned was how<br>to use the WTF (What The Form) extension to create forms with custom<br>validations for input fields. The extension comes with built-in validators, but I also<br>learned how to write custom validators to ensure that the user's inputs met<br>the requirements for each field. Additionally, I learned how to use backend validation<br>to further validate user inputs and catch errors that might otherwise have gone<br>unnoticed.</div><div><br></div><div>3. One of the most important things I learned was how to write<br>SQL queries to solve problems related to web development. SQL is a powerful<br>language for managing and querying relational databases, and I learned how to use<br>it to retrieve and manipulate data from tables, as well as how to<br>join multiple tables to create more complex queries. This skill proved to be<br>invaluable when working on projects that required the manipulation of large datasets or<br>the extraction of specific information from a database.</div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/kb97" target="_blank">Grading</a></td></tr></table>