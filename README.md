emailer
---
Python email package to send emails based off of jinja templates

### Installation
---
Install using pip:

    $ pip install -e git+git://github.com/cmeadows/emailer.git

Install using setuptools:

    $ git clone https://github.com/cmeadows/emailer.git
    $ python setup.py install

### Usage
---

#### Basic Usage

```python
from emailer import Emailer, Message

e = Emailer()
e.configure_server(SMTP_SERVER_HOST, SMTP_SERVER_PORT, user=SMTP_SERVER_USER, password=SMTP_SERVER_PASSWORD)

m = Message(from_email=YOUR_FROM_EMAIL, to_email=YOUR_TO_EMAIL, subject=YOUR_SUBJECT)

e.send_message(m)
```

#### Email Using TemplateManager

```python
from emailer import TemplateManager

manager = TemplateManager(YOUR_TEMPLATE_DIR)
# Replace var1, var2, etc for your template variables
email_html = manager.render_template(TEMPLATE_FILENAME, file_name=var1="var1", var2="var2")

m = Message(from_email=YOUR_FROM_EMAIL, to_email=YOUR_TO_EMAIL, subject=YOUR_SUBJECT, html=email_html)

e.send_message(m)
```

### License
---
The MIT License (MIT)

Copyright (c) 2016 Collin Meadows

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
