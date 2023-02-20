<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Kush Sudhir Borikar (kb97)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 6:31:38 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/kb97" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/219473425-f8d56ae9-cb64-4995-9d83-eef2c16d4d3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the part of the code which shows the function add-task,<br>this code function updates last activity, it adds the task if all the<br>three inputs are non empty fields, and does not add the task if<br>even one field is an empty one.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/219474993-3bd9f31f-afbb-4896-a6bf-96b1d7b02345.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows Added task and Adding failed <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>1.&nbsp;<span style="font-size: 13px;">update lastActivity with the current datetime value - the lastActivity is<br>used to show the latests activity performed on any particular task. It is<br>done using the datetime python library.</span><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">2. Add new task<br>to the list</span><span style="font-size: 13px;">- all the fields provided by user are&nbsp; added<br>as a task&nbsp;</span><br></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">3. The program makes sure due date<br>is matching the formats in str_to_datetime</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">4. Output message confirming<br>the new task was added was printed&nbsp;</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">5.save() function was<br>called&nbsp;&nbsp;</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/219479338-0ee9f0bb-c483-4d13-b16e-2c6d4d84f8d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the function code that pulls index value and also checks<br>for the index value to be out of bound or not, if it<br>is in bound, we can update the task, if index out of bounds,<br>task cannot be updated. Once update is possible we can see in output<br>the existing task fields as well.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>The process_update function takes index value as an input and checks it against<br>the bounds, if in bounds, we can perform update in the next function,<br>if not update cannot be performed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220152679-d5266450-2f1b-4286-9aef-c026bab6ef78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This snippet of code shows how tasks are found by index and how<br>index in and out of bounds scenarios are handled. It shows output of<br>cases where tasks is updated and not updated as well.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220153404-2f1df37c-1142-4a1d-8855-dc0d540efbdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output of a successful update and output of a<br>failed update as well, as requested.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">1. find the task by index - tasks are found by<br>index passed to the update function using an if condition statement</span><div><span style="font-size: 13px;"><br></span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;2. Index out of bounds scenarios were handled using a if statement<br>again but by using the len(tasks) method to ensure index is in bounds</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<br></span></div><div><span style="font-size: 13px;">3. Incoming task was update in case of all data<br>being provided</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">4.</span><span style="font-size: 13px;">&nbsp;</span><span style="font-size: 13px;">the lastActivity is used<br>to show the latests activity performed on any particular task. It is done<br>using the datetime python library.</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">5. A message saying the<br>task was not updated was printed in the scenario of a missing input.</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<br></span></div><div><span style="font-size: 13px;">6. Save function was called and student details were mentioned<br>in the comment</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220155112-5e1236e9-6646-430e-868c-eaddd0a65b70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This snippet of code shows how tasks are found by index and how<br>index in and out of bounds scenarios are handled. A task is marked<br>as done if it&#39;s done value was false before and updated with current<br>date and time using datetime library. If a task is already completed, that<br>is it&#39;s done value has date and time already, we will print &quot;task<br>already completed&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220156325-a11a759f-de0c-43a5-80b4-b3a9bec2379e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output of a successful mark done of a task.<br>And also output showing how a task has been already updated in case<br>if it was already marked done before.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">&nbsp;</span><span style="font-size: 13px;">1. find the task by index - tasks are<br>found by index passed to the update function using an if condition statement</span><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<br></span></div><div><span style="font-size: 13px;">2. Index out of bounds scenarios were handled using a<br>if statement again but by using the len(tasks) method to ensure index is<br>in bounds</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">3. when done option is entered, the done<br>value of a task if false is updated with the current datetime value<br>and output of a successful mark done is printed</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">4.<br>When done option is entered, if the done value of a task already<br>contains a datetime value, it will not change anything an out will be<br>printed saying that task is already completed.</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">5. Save function<br>was called and student details were mentioned in the comment</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220161655-e54c7fbe-11e1-4117-ac2a-2b9c62b0e2af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows snippet of code for the view_task function and the output when<br>this options is entered.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220161795-86c904ec-7345-402e-bc00-508c8493ab21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output shows the successful display of a task indexed within bounds, and also<br>output of value that is out of index bounds.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220161969-05124f0c-d61a-41ea-bfc6-ff0c26efb147.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of the option list displays all the tasks in the list.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220163424-0b97e3ae-0f19-49c3-8538-8841a09d637f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the snippet of a code of the delete_task function. It<br>deletes the task by index that is passed to the function, it also<br>handles out and in bounds scenarios.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220163880-efd1abd3-8189-477e-9091-0027b4915e5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output shows successful deletion of a task which is in index and present<br>in list, and also output of an index out of bounds scenario, since<br>that task is not in list.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-size: 13px;">1.delete/remove tasks was handled by passing index to the function and<br>checking if that index exists in the list, if it exists, that task<br>was deleted, if that index did not exist in the list, no tasks<br>was deleted and a message printing index out of bounds is printed.</span></div><div><span style="font-size:<br>13px;"><br></span></div><div><span style="font-size: 13px;">2. Message is shown for both scenarios of a successful delete<br>and a failed delete.</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">3. Index out of bounds scenarios<br>were handled using a if statement again but by using the len(tasks) method<br>to ensure index is in bounds</span><span style="font-size: 13px;"><br></span></div><span style="font-size: 13px;"><div><span style="font-size: 13px;"><br></span></div>4. Save<br>function was called and student details were mentioned in the comment</span><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220165791-2d072ccc-5de7-4042-9e6b-ebb9d25a8b6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the snippet of code that shows the list of incomplete<br>tasks as an output.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220166019-e62b5bfc-39cf-4bfc-a3b2-fcd1add6b62f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success in showing any incomplete tasks in the list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220166540-1d73247d-1c2b-42b6-a71a-2c547b067ef9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success in showing no incomplete tasks as there are no incomplete tasks in<br>the list.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>we check for all indexes in the list, and see if any<br>index has their done value as false, if this condition is true, these<br>indexes will will appended to the list &quot;_tasks&quot;, and then this list is<br>listed using list_tasks, this shows a list of all incomplete tasks present in<br>a list.<div><br></div><div>2. If there are no incomplete tasks, it will print &quot;No tasks<br>to show&quot;</div><div><br></div><div>3. Student details are added as a comment</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220172047-b7fc284a-ee36-4441-8ae7-7852aaa5a91c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows snippet of code function get_overdue_tasks, which prints tasks which have due<br>date older than the current date, hence overdue<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220172707-60b4fd7d-b978-4c85-96af-df1e2f5325f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output prints list of overdue tasks, which in this case is 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220172788-a85e4958-760c-45d1-9f32-a38841f6a051.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output prints no tasks to show as all tasks are complete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>1. The if condition compares the current time with the due date, if<br>current time is greater than due date, it will be added to "_tasks"<br>list.</div><div><br></div><div>2. The "_tasks" list will be displayed using list_tasks() function</div><div><br></div>3. Student details are<br>added as a comment<br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220209122-2fd0a5d9-0999-40f1-b485-a4ae4b077587.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the snippet of code that prints the remaining time for<br>a due date or the time that has passed since a due date<br>by taking index as an argument.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220209359-702c9c04-0e39-46b3-8d1f-3cc27eeba411.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output showing how many days, hours, minutes, seconds until due and also how<br>much it is overdue by.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">&nbsp;</span><span style="font-size: 13px;">1. the tasks are fetched by passing index as<br>an argument to the get_remaining_time function&nbsp;</span><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">2. Index out of<br>bounds scenarios were handled using a if statement again but by using the<br>len(tasks) method to ensure index is in bounds</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">3. the<br>remaining time to due date is found by subtracting the due date from<br>current datetime and printed using a print statement and placeholders</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size:<br>13px;">4. to handle the overdue scenario, we substract the current datetime from the<br>due date to get the days and hours the task is overdue by.</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<br></span></div><div><span style="font-size: 13px;">5. student details are entered as a comment</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220210785-e031e1c8-4920-4f3a-8289-ea82c40aabd1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1 of Program Outputs<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220211061-5d4c6b91-a923-47c5-bfaa-b172a50329d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2 of Program Outputs<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220211398-8584a071-eb99-4567-9314-96f07ed59f60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2 of Program Outputs<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123112921/220211522-55fd81bb-4014-47ea-b5fa-839a90a51b91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of JSON file showing varying outputs<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>I learned about a new python library that is &quot;datetime&quot;. I also faced<br>some issue while converting date from string format to datetime format, but after<br>reviewing the code and str_to_date time function carefully, I was able to figure<br>it out.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/kush0698/IS601-004/pull/6">https://github.com/kush0698/IS601-004/pull/6</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/kb97" target="_blank">Grading</a></td></tr></table>