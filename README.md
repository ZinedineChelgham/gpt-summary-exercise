## My approach

I chose to create a Python-based service that efficiently
processes requests to generate and serve
astronomical time-domain research summaries.
The system is designed to cater to both known and unknown users,
ensuring secure and authorized access to the generated reports.

### Core Features:

- User Authentication (in a simplified way): The service distinguishes between known and unknown users.
  Known users (user1, user2, user3) are allowed to request summaries.
  Unauthorized users receive an error message, ensuring data security and controlled access.

- Data Processing: The service utilizes OpenAI's GPT model for processing and summarizing astronomical data.
  This involves transforming raw data into a more readable and comprehensive format, specifically tailored for
  professional astronomers.

- Responsive Web Interface: Users interact with the service through a web interface (summary.html), where they can enter
  a user ID and request a summary.

### Installing

- ``` pip install -r requirements.txt ```
- Specify your OPENAI_KEY on a .env file in the same directory as main.py

### Running

- ``` python main.py ``` (server will start on port 8080)
- Open summary.html in your browser
- Specify a userid good ones are (user1, user2, user3)
- Submit and enjoy the report !

### Possible improvements

- Fine tune the model on actual good reports
- Consider scalability and load balancing for handling a high number of simultaneous requests.
- Consider security and authentication for the web interface.
- Enhance user authentication to support a broader range of users with secure login mechanisms.

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Flask](http://flask.pocoo.org/) - The web framework used
* [OpenAI](https://openai.com/) - The GPT model used


