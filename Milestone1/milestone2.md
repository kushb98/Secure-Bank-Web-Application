<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Bank Project</td></tr>
<tr><td> <em>Student: </em> Kush Sudhir Borikar (kb97)</td></tr>
<tr><td> <em>Generated: </em> 4/30/2023 12:09:09 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-bank-project/grade/kb97" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Create Accounts table and setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot from the db of the system user (Users table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235318347-27fbf3b4-65e4-4feb-a373-780a9084ae03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the system user in user table in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot from the db of the world account (Accounts table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235318386-e818c641-ce07-4e4a-b308-838a1b6162bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the world account in the account table in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain the purpose and usage of these two entries and how they relate</td></tr>
<tr><td> <em>Response:</em> <p>To carry out any transactions such as deposit, withdrawal, or transfer, <br>it is<br>essential to have a user account. This is because the user_id in <br>the<br>accounts table is a foreign key that references the user to whom the<br><br>account belongs. Similarly, the src and dest fields in the Transactions<br> table are<br>foreign keys that refer to the unique id of the accounts <br>table. Therefore,<br>to perform any transaction, these entries in the <br>accounts and transactions tables are<br>necessary. Without them, it would <br>not be possible to link the transaction to<br>a specific user or account.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/25">https://github.com/kush0698/IS601-004/pull/25</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Dashboard </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the requested links/navigation</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235322265-4cb5edc3-6369-48c8-8ef4-f591bbea15d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing NAV bar dropdown<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235322291-044e8d25-3123-4652-acc5-19b20bbf7699.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Create Account form working from the NAV bar<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235322346-7a21bfd6-3080-4b9b-b03b-1b30c01d04d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing My Account working from the NAV bar<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain which ones are working for this milestone</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Create Account Link -&nbsp;<u><a href="https://is601-kb97-dev.herokuapp.com/accounts/create">https://is601-kb97-dev.herokuapp.com/accounts/create</a></u><br><br>2) My Account Link -&nbsp;<u><a href="https://is601-kb97-dev.herokuapp.com/accounts/list">https://is601-kb97-dev.herokuapp.com/accounts/list</a></u><br><br>The above are the working<br>links.<br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/26">https://github.com/kush0698/IS601-004/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Create a checking Account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the Create Account Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235334125-964980b8-324e-4981-9b6c-f19c80ffb3c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows valid data filled in and heroku dev URL<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots showing validation errors and success message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235334146-cdf328e2-3952-439d-9d47-4aef9e6d0a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows minimum funding validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235334167-c5a3713c-72fa-444b-90bc-053b56f32fdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the success message from task 1 &#39;s data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the transaction generated from the initial deposit (from the DB)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235334190-af76085b-e32c-4a6f-83c2-48208467c9ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows Transaction Table with above performed account opening transactions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain which account number generation you used and the account creation process including the transaction logic</td></tr>
<tr><td> <em>Response:</em> <ol><br><li><p>I used option number 2 for generating an Account number -&nbsp;<span id="docs-internal-guid-b0b81fe3-7fff-683c-d463-6c92b83c355b">&lt;span<br>style=&quot;font-size: 11pt; font-family: Arial; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates:<br>normal; vertical-align: baseline; white-space: pre-wrap;&quot;&gt;Option 2: </span><span style="font-size: 11pt; font-family: Arial; background-color: transparent;<br>font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; vertical-align: baseline; white-space: pre-wrap;">Generate the number based<br>on the id column; requires inserting a null first to get the last<br>insert id, then update the record immediately after</p><br></li><br><li><p>The code creates an account<br>for a user with an associated account number, inserts a starting balance, and<br>generates two transaction records: one for the deposit and one for the withdraw.<br>The account number is generated based on the id column of the last<br>inserted record. The transactions are generated for both the source and destination accounts,<br>and the account balances are refreshed to reflect the changes.</span></span><br></p><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/27">https://github.com/kush0698/IS601-004/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/accounts/create">https://is601-kb97-prod.herokuapp.com/accounts/create</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to list their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's account list view (show 5 accounts)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235334965-2db74d18-2605-4532-8ad2-3d1228831253.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows 5 accounts in list and account number, account type, modified and<br>balance<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the page is displayed and the data lookup occurs</td></tr>
<tr><td> <em>Response:</em> <p>This code selects all accounts of the logged-in user from the database by<br>using a select query with a WHERE clause to filter by the user<br>ID stored in the session. The query returns a list of dictionaries, which<br>is passed to a Jinja template where it is iterated and the values<br>are displayed in respective rows.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/29">https://github.com/kush0698/IS601-004/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/accounts/list">https://is601-kb97-prod.herokuapp.com/accounts/list</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Account Transaction Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of an account's transaction history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235336436-dff56c13-1a0b-423a-82bf-1de03ba68417.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows transactions and the page for account 000000000005 with the required fields<br>and columns from the tables<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235336463-ec13de6a-b998-442b-b8e7-06b608c960a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows transactions and the page for account 000000000006 with the required fields<br>and columns from the tables<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the lookup and display occurs</td></tr>
<tr><td> <em>Response:</em> <p>To display the transactions of a specific account, we use a select query<br><br>to retrieve records from a table that contain the account ID in either<br><br>the &quot;src&quot; or &quot;dest&quot; columns. This allows us to display all transactions <br>that<br>involve the account, whether it was the source or destination of <br>the transaction.<br>By using this approach, we can ensure that all relevant<br> transactions are displayed<br>in a single view, without needing to make <br>separate queries for each type<br>of transaction. This can be particularly <br>useful for users who want to review<br>their account activity in a <br>comprehensive and efficient manner.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/31">https://github.com/kush0698/IS601-004/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/accounts/transactions?acc_number=000000000006&start_date=&end_date=">https://is601-kb97-prod.herokuapp.com/accounts/transactions?acc_number=000000000006&start_date=&end_date=</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Deposit/Withdraw </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a Screenshot of the Deposit Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235337515-48a78046-b735-4f1f-9a3b-3fe2c8b5bacb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Valid data filled in for deposit page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a Screenshot of the Withdraw Page (this potentially can be the same page with different views)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235337588-44802d63-8d2b-4def-94cd-43a6ffbcbcc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the dropdown of logged in user&#39;s accounts<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235337668-1c694c17-ac95-44ca-9612-f195520cffdc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Valid data filled in for withdraw page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show validation error for negative numbers</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235337736-cc57d67e-504b-41c2-806c-d8422a9166c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows website validation for negative numbers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Show validation error for withdrawing more than the account contains</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235362274-486f4905-6792-4d6e-b1ef-cc92c94ee74c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Shows validation error for withdrawing more than the account contains<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Show a success message for deposit and withdraw (2 screenshots)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235362502-4ee54d07-4a85-47ff-84b6-ffe84b086677.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows a success message for deposit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235362638-7395ab25-48a0-45e7-b98a-ebd33fced7dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows a success message for withdraw.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Show a screenshot of the transaction pairs in the DB for the above tests</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/235362899-ecd411aa-cf9e-4b9c-9c46-d0218787dec9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the pair of the transaction in the DB for the above<br>tests.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain how transactions work</td></tr>
<tr><td> <em>Response:</em> <p>To perform deposit or withdraw operation on an account, two queries are executed.<br>The first query updates the balance in the accounts table while the second<br>query makes a new entry in the transactions table. The source and destination<br>for deposit and withdraw are the same, which is the account ID of<br>the corresponding account. In the case of deposit, the difference value is inserted<br>with a positive sign, whereas for withdraw, the difference value is inserted with<br>a negative sign.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/33">https://github.com/kush0698/IS601-004/pull/33</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/accounts/deposit">https://is601-kb97-prod.herokuapp.com/accounts/deposit</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/accounts/withdraw">https://is601-kb97-prod.herokuapp.com/accounts/withdraw</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>1) I gained knowledge on various techniques for passing data between different pages,<br>including passing arguments or using session data to maintain user information.</div><div><br></div><div>2) I learned<br>how to use the WTForms library to create forms with built-in validation and<br>how to implement backend validation for input fields to ensure data accuracy and<br>completeness.</div><div><br></div><div>3) I also learned how to apply SQL queries on a given problem<br>statement to interact with a database and retrieve relevant information for the user.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/login">https://is601-kb97-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-bank-project/grade/kb97" target="_blank">Grading</a></td></tr></table>