<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Kush Sudhir Borikar (kb97)</td></tr>
<tr><td> <em>Generated: </em> 4/26/2023 10:12:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/kb97" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234358906-98225788-3b1e-4816-b440-12896899d260.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows invalid email has been entered.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234359210-fbe2b600-9b46-4ac3-9661-62f4f7656b75.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows password validation and matching<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234359507-1c5ef532-c484-4d03-a4b5-e6954f158cda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows User ID or Email is already taken.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234359778-3814ddcf-59ea-402a-888d-21f3f4b24bd1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows form with valid data filled in before the form is submitted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234349567-bf17fcf5-f1a3-42e0-81bf-54ee8575a1f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Valid user data from Task 1 - ROW 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/21/">https://github.com/kush0698/IS601-004/pull/21/</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>We develop a form class that derives from FlaskForm and implements WTF. Fields,<br>field types, and validations are defined in this class. Now, all we have<br>to do is access form fields and deliver the request in our endpoint<br>function by using the form object.WTF forms typically handle the internal validation defined<br>in the aforementioned custom form class on the client side. But even on<br>the server side, we use the WTF form method valid_on_submit() to once more<br>validate the form fields. The form object is sent to the frontend, where<br>the validation error is displayed, if any validation fails right away. Validation errors<br>are then stored in the form object&#39;s errors field.&nbsp;WTF forms typically handle the<br>internal validation defined in the aforementioned custom form class on the client side.<br>But even on the server side, we use the WTF form method valid_on_submit()<br>to once more validate the form fields. The form object is sent to<br>the frontend, where the validation error is displayed, if any validation fails right<br>away. Validation errors are then stored in the form object&#39;s errors field.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234731504-b7e8007d-3be9-44a4-bb3c-e3bade5822e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the flash message for password mismatch with DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234732189-aaafbae9-fe6f-4eb2-9ea5-53988b7627ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows a flash message that display login success.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/21/">https://github.com/kush0698/IS601-004/pull/21/</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>We develop a form class that derives from FlaskForm and implements WTF. Fields,<br>field types, and validations are defined in this class. Now, all we have<br>to do is access form fields and deliver the request in our endpoint<br>function by using the form object.WTF forms typically handle the internal validation defined<br>in the aforementioned custom form class on the client side. But even on<br>the server side, we use the WTF form method valid_on_submit() to once more<br>validate the form fields. The form object is sent to the frontend, where<br>the validation error is displayed, if any validation fails right away. Validation errors<br>are then stored in the form object&#39;s errors field.The hashed value of the<br>password is first stored in the database before it is first hashed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234732568-246f9b26-0bd3-4358-8030-742109d3cfae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows a flash message that display logout success.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234732765-0ff008a4-a816-413e-aad7-dff3458254d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/21/">https://github.com/kush0698/IS601-004/pull/21/</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Any time a user tries to visit a login-protected page, the session data<br>is checked to see if the user is authenticated; if not, the is_authenticated<br>flag remains false and the user is prevented from accessing the login-protected pages.<br>Basically, the session is set anytime a person logs in with their username,<br>email, password, and roles. The user will be able to access the login-protected<br>website during that period without having to log in since the session is<br>brief and only valid for 30 minutes.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234732765-0ff008a4-a816-413e-aad7-dff3458254d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234734587-f969acb6-9089-4eec-9153-a0611f80213e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows permission denied to a user who does  not have the<br>privileges of the admin role.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234735188-8299bf99-73cc-4bbd-bd19-6449873edd40.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234734933-7ad1002e-cc4f-4ab2-8521-3d49e7752ec3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of the User_Roles table with valid data. Admin is the user<br>with role_id as -1.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/21/">https://github.com/kush0698/IS601-004/pull/21/</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>When a user tries to access a login-protected page, their session data <br>is<br>checked to see if they have already authenticated themselves. If the <br>user hasn&#39;t<br>logged in yet, the &quot;is_authenticated&quot; flag remains false and<br> they won&#39;t be able<br>to access the protected pages. When a user logs in, <br>their session is<br>set with details such as their username, email, <br>password, and roles. This session<br>is temporary and lasts for 30 minutes.<br> During this time, the user can<br>access the protected pages without <br>having to log in again.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Similarly to the login process, the user&#39;s roles are also stored in their<br>session data. When a user attempts to access a page protected by specific<br>roles, they will be denied access if they don&#39;t have the required role.<br>In the jinja template, we check the user&#39;s role and render the appropriate<br>UI based on that role. Certain functions are only visible and accessible to<br>admin users who have the necessary role.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234737130-82982fed-d822-4cb5-b95a-bb15e66d84c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of User Registration Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234737838-6403b546-85fb-4bb1-8234-4c6ccd8d273e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of User Login Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234737996-d66118c2-1987-4d4a-b546-78c4d539cfc9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of User Profile Edit Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234738294-247dc7b2-51e3-4971-869d-7593dd60d9ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of Role List page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234738447-f6abc29d-e37e-4984-b02e-676356324c8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of Role Assign page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/21/">https://github.com/kush0698/IS601-004/pull/21/</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>The built-in form classes utilize their internal styling to style the <br>forms. The<br>navigation class is used for navigation, and its styles are <br>inherited.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234731504-b7e8007d-3be9-44a4-bb3c-e3bade5822e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the flash message for password mismatch with DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234732765-0ff008a4-a816-413e-aad7-dff3458254d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234734587-f969acb6-9089-4eec-9153-a0611f80213e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows permission denied to a user who does  not have the<br>privileges of the admin role.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/21/">https://github.com/kush0698/IS601-004/pull/21/</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>To handle situations where an email or username already exists, the update or<br>insert statement throws a duplicate key error which is caught by an except<br>block. Within the except block, the regular expression search method is used to<br>check if the duplicate word, username, or email already exists. If it does,<br>a user-friendly message is displayed informing the user that the username or email<br>is already taken.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234739533-d5bab6aa-718e-4ea9-a558-d146c7237128.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows prefilled email and username is visible properly <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/21/">https://github.com/kush0698/IS601-004/pull/21/</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The user data is retrieved from the session data that was set during<br>login. The session data is then converted into a dictionary using the json.loads()<br>function. The dictionary items are then passed into the user object. The filled<br>user object is then passed into the form object, which internally pre-fills the<br>data using WTF forms.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234739924-69bff969-33fe-4780-a00f-176ffb72bdd6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows username validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234740093-ec248bd1-8964-4242-a501-5b0a460c0b33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234740799-d478bce3-284a-4a6e-b2b0-fc972c4f7afe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email/username already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234741183-93296cc8-3a8e-4bae-bb48-32d403f7e6be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB before updation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/234741322-e6c318e7-8773-4608-810f-da37ac591670.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB after updation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/21/">https://github.com/kush0698/IS601-004/pull/21/</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>1) Two separate forms have been created, one for editing username and email,<br>and the other for changing the password.</div><div>2) Two new form classes have been<br>added to forms.py and added to the landing page of the user.</div><div>3) The<br>username and email are pre-filled from the session data that was set during<br>the login endpoint. The user enters their desired username and password in the<br>form. If the old username and email are the same as the session<br>data, no update is performed. If they are different, an update query is<br>executed. If the update is successful, the session is also updated. If the<br>user enters an existing username as their desired new username/email, a duplicate key<br>error is thrown. This error is caught using an except block and a<br>user-friendly message is displayed.</div><div>4) For the second form, which is for changing the<br>user's password, if the old password entered by the user doesn't match, a<br>friendly message is shown. If the password matches the original password from the<br>session, then only the password is changed.</div><div>5) The forms classes created specify the<br>validations, which are internally handled by WTF forms. For validations such as username/email<br>already taken, a duplicate key error is caught, and a proper user-friendly message<br>is displayed.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>1) During my learning experience, I gained knowledge about sessions, which allowed me<br>to manage user logins and store data in sessions rather than querying the<br>database repeatedly for the same data. I also learned how to use the<br>flask_login package to implement user login and logout mechanisms, as well as the<br>flask principle package to implement roles in Flask.</div><div>2) Additionally, I learned how to<br>prefill and add validations to input fields using WTF forms, and how to<br>perform backed validation.&nbsp;</div><div><br></div><div>I encountered some problems during the process:</div><div>1) I faced an "invalid<br>salt" error when attempting to update a user's password. This was due to<br>me not including the hidden tag in the password update form.</div><div>2) I noticed<br>that when I updated the user's username or email on the landing page,<br>the database would reflect the changes, but the landing page would still display<br>the old username/email taken from session data. To resolve this issue, I updated<br>the session data whenever the user updated their username or email.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kb97-prod.herokuapp.com/">https://is601-kb97-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/kb97" target="_blank">Grading</a></td></tr></table>