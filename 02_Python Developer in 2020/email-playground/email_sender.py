import smtplib # Simple Mail Transfer Protocol
from email.message import EmailMessage
from string import templae
from pathlib import Path # os.path


html = Templae(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Kay Kozaronek"
email["to"] = "juliet.gurdie@gmail.com"
email["subject"] = "You won 1.000.000 dollars!"

email.set_content(html.substitute({name="TinTin"}, html)

with smtplib.SMTP(host="smtp.gmail.com", port =587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("kozaronek@gmail.com", "INPUT PASSWORD HERE")
	smtp.send_message(email)
	print("all good boss!")
