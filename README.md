
<h1>SMS Broadcasting Auto-replying App</h1>
<p>Arian Aghnaei</p>
<p>Feb 2020</p>
<p>Python 3.8</p>
<hr />
<h2>SMS automated broadcasting service</h2>
<p>In this porject I used twilio api to send bulk text messages to multiple phone numbers. I also used Flas framework to auto reply to messages from the users it means when the user sends back a specific answer (That is mentioned in first sms to user) the flask app and Twilio will answer to the replied message.</p>
<p>The other cool thing about this broadcasting app, is it's blacklisting functionallity. It means if any of the clients do not want to recieve broadcasting messages from sender anymore, the user can easily do it by sending a spcific answer to sender's number and the reciever's number will be added to the blocklist.</p>
<p>This project is a command line application.</p>

<p>We can use emajies in message body and we can also send media files in the messasges by specifying image source in the message body and Twilio renders it to display in the user phone.</p>
<hr />
<h2>What I learned :</h2>
<ul>
  <li>How to use Flask API to create a automated service that is interactable.</li>
  <li>Attaching media to the text message body.</li>
  <li>Create a auto replying system that will send different responses depending on users message.</li>
  <li>Using all these seprated functionallities to run a autoreplying broadcasting SMS system.</li>
  <li>Running different functions depending replyies from the user like black listing or sending extra data in  message form.</li>
</ul>
<br>
<hr />
<h2>How to use</h2>

<ol>
  <li>Update sender phonoe number data in full_app_finall.py (line 26).</li>
  <li>Update account sid credentials in line 19 (You can access your sid number from twilio account dashboard.)</li>
  <li>Add the phone numbers you want to recieve the messages to the numbers.csv file in the project directory. Use following format (+11234567890)</li>
  <li>Add your Twillio phone number and Twilio auth token to the my_secret_numbers.py file in the project directory.</li>
  <li>After doing all the above steps and making sure target phone number is not in the blacklist.csv file by accident!!!</li>
  <li>Now you are goot go, so open the terminal and navigate to the project directory and run the following command:    python full_app_final.py</li>
</ol>
<hr />
<p>The code is fully commented so you can use for learning and also your personal projects.</p>
<p>I really want to know what other developers like you are thinking about my code so don't hesitete to contact me and share your idea about this piece of code.</p>
