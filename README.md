# 🌟 Welcome to DailyMoodBoost! 🌟
Welcome to DailyMoodBoost, your personalized SMS service to stay motivated, entertained, and organized. Use the following commands to subscribe, customize, or stop services at your convenience. Explore our four fantastic features and make every day count!
# Imstruction:
1. WATER: Stay hydrated and refreshed.
Subscribe: Send JOIN WATER to start receiving reminders to drink water.
Customize Times: Use CS WATER <time1> <time2> <time3> to set your preferred reminder times (e.g., CS WATER 08:00 12:00 18:00).
Leave the Service: Send LEAVE WATER to stop receiving reminders.

3. JOKE: Add humor to your day.
Subscribe: Send JOIN JOKE to start receiving 3 daily jokes.
Customize Time: Use CS JOKE <time> to set the delivery time for your jokes (e.g., CS JOKE 15:00).
Instant Joke: Send JOKE anytime for a quick laugh.

5. QUOTE: Stay motivated and inspired.
Subscribe: Send JOIN QUOTE to start receiving 3 daily inspirational quotes.
Instant Quote: Send QUOTE anytime to receive an immediate quote.

7. Match Scores: Never miss the latest sports updates.
Get Scores: Send GAME <team name> to receive live updates about your favorite teams (e.g., GAME Hamburger SV).

9. General Commands:
Subscribe to All: Send SUBSCRIBE DailyMoodBoost to join all available services at once.
View Status: Send STATUS to see the list of services you're currently subscribed to.
Unsubscribe All: Send UNSUBSCRIBE DailyMoodBoost to leave all services.

## 📍 Overview

A versatile SMS notification system that integrates external APIs to provide engaging and automated messaging experiences. This project combines SMS management, joke retrieval, and database functionality to create a unique communication platform.

## 👾 Features

- 📱 SMS sending capabilities with flexible management
- 🤣 Random joke retrieval from external API
- 💾 SQLite database integration for persistent storage
- 🔗 Modular architecture with clear separation of concerns
- 🚀 Easy configuration and extensibility

## 📁 Project Structure

```sh
└── hackathon-group-1/
    ├── README.md
    ├── __pycache__
    │   └── config.cpython-312.pyc
    ├── config.py
    ├── data_managers
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── sms_manager.py
    │   └── sqlite_manager.py
    ├── database
    │   ├── __pycache__
    │   ├── dailyMoodBoost.sqlite
    │   ├── extension.py
    │   └── init.py
    ├── external_api
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── jokes.py
    │   ├── match.py
    │   └── quotes.py
    ├── handlers
    │   ├── __init__.py
    │   ├── change_scheduler.py
    │   ├── handle_drink_response.py
    │   ├── join_channel.py
    │   ├── leave_channel.py
    │   ├── status_response.py
    │   ├── subscribe_team.py
    │   └── unsubscribe_team.py
    ├── main.py
    ├── requirements.txt
    ├── schemas
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── _base.py
    │   ├── channel_schema.py
    │   ├── custom_schedule.py
    │   ├── jokes_schema.py
    │   ├── message_schema.py
    │   ├── subscription_schema.py
    │   └── user_schema.py
    ├── sms_responses.py
    ├── task_scheduler
    │   ├── __init__.py
    │   ├── broadcasts.py
    │   └── task_scheduler.py
    └── utils
        ├── __pycache__
        ├── dates.py
        ├── decorators.py
        ├── information.py
        ├── to_dict_mixin_schema.py
        └── validation.py
```

### 📂 Project Index
<details open>
<summary><b><code>HACKATHON-GROUP-1/</code></b></summary>
<details> <summary><b>__root__</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/sms_responses.py'>sms_responses.py</a></b></td>
<td>Contains the response messages for the SMS service.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/config.py'>config.py</a></b></td>
<td>Contains the configuration settings for the application, including API endpoints, credentials, and constants.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/main.py'>main.py</a></b></td>
<td>The main entry point of the application. It handles incoming SMS messages, processes them, and sends responses.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/requirements.txt'>requirements.txt</a></b></td>
<td>Lists the project dependencies, such as the libraries and packages required to run the application.</td>
</tr>
</table>
</blockquote>
</details>
<details> <summary><b>handlers</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/handlers/leave_channel.py'>leave_channel.py</a></b></td>
<td>Contains the logic for unsubscribing users from SMS channels.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/handlers/unsubscribe_team.py'>unsubscribe_team.py</a></b></td>
<td>Contains the logic for unsubscribing users from SMS channels.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/handlers/handle_drink_response.py'>handle_drink_response.py</a></b></td>
<td>Contains the logic for handling responses related to drink reminders.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/handlers/change_scheduler.py'>change_scheduler.py</a></b></td>
<td>Contains the logic for allowing users to change the schedule of their SMS reminders.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/handlers/status_response.py'>status_response.py</a></b></td>
<td>Contains the logic for sending the status of subscriptions to users.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/handlers/join_channel.py'>join_channel.py</a></b></td>
<td>Contains the logic for subscribing users to SMS channels.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/handlers/subscribe_team.py'>subscribe_team.py</a></b></td>
<td>Contains the logic for subscribing users to SMS channels.</td>
</tr>
</table>
</blockquote>
</details>
<details> <summary><b>schemas</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/schemas/user_schema.py'>user_schema.py</a></b></td>
<td>Defines the database schema for users, including phone number and timestamps.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/schemas/subscription_schema.py'>subscription_schema.py</a></b></td>
<td>Defines the database schema for subscriptions, linking users to channels.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/schemas/_base.py'>_base.py</a></b></td>
<td>Defines the base class for database schemas, including common fields and methods.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/schemas/message_schema.py'>message_schema.py</a></b></td>
<td>Defines the database schema for messages, including sender, content, and timestamps.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/schemas/jokes_schema.py'>jokes_schema.py</a></b></td>
<td>Defines the database schema for jokes, including the joke text and timestamps.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/schemas/custom_schedule.py'>custom_schedule.py</a></b></td>
<td>Defines the database schema for custom schedules, allowing users to personalize their reminder timings.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/schemas/channel_schema.py'>channel_schema.py</a></b></td>
<td>Defines the database schema for channels, including channel name and ID.</td>
</tr>
</table>
</blockquote>
</details>
<details> <summary><b>task_scheduler</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/task_scheduler/task_scheduler.py'>task_scheduler.py</a></b></td>
<td>Contains the task scheduler, responsible for sending scheduled messages and managing scheduled tasks.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/task_scheduler/broadcasts.py'>broadcasts.py</a></b></td>
<td>Contains the logic for broadcasting messages to subscribed users.</td>
</tr>
</table>
</blockquote>
</details>
<details> <summary><b>data_managers</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/data_managers/sqlite_manager.py'>sqlite_manager.py</a></b></td>
<td>Manages interactions with the SQLite database, handling data storage and retrieval.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/data_managers/sms_manager.py'>sms_manager.py</a></b></td>
<td>Manages sending and receiving SMS messages through the Masterschool SMS API.</td>
</tr>
</table>
</blockquote>
</details>
<details> <summary><b>utils</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/utils/dates.py'>dates.py</a></b></td>
<td>Provides utility functions for handling dates and times.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/utils/information.py'>information.py</a></b></td>
<td>Provides utility functions for handling information and printing messages.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/utils/validation.py'>validation.py</a></b></td>
<td>Provides utility functions for validating data, such as incoming SMS messages.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/utils/decorators.py'>decorators.py</a></b></td>
<td>Provides decorators for modifying the behavior of functions.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/utils/to_dict_mixin_schema.py'>to_dict_mixin_schema.py</a></b></td>
<td>Provides a mixin class for converting database objects to dictionaries.</td>
</tr>
</table>
</blockquote>
</details>
<details> <summary><b>external_api</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/external_api/jokes.py'>jokes.py</a></b></td>
<td>Provides functions for fetching jokes from an external API.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/external_api/match.py'>match.py</a></b></td>
<td>Provides functions for fetching football match data from an external API.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/external_api/quotes.py'>quotes.py</a></b></td>
<td>Provides functions for fetching quotes from an external API.</td>
</tr>
</table>
</blockquote>
</details>
<details> <summary><b>database</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/database/extension.py'>extension.py</a></b></td>
<td>Provides extensions and configurations for the database.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/database/init.py'>init.py</a></b></td>
<td>Initializes the database and sets up the database schema.</td>
</tr>
<tr>
<td><b><a href='https://github.com/saifmasterschool/hackathon-group-1/blob/master/database/dailyMoodBoost.sqlite'>dailyMoodBoost.sqlite</a></b></td>
<td>The SQLite database file used to store application data.</td>
</tr>
</table>
</blockquote>
</details>
</details>

## 📌 Project Roadmap

- [X] **`Task 1`**: Set up core project structure
- [X] **`Task 2`**: Implement SMS sending functionality
- [X] **`Task 3`**: Integrate external joke API
- [ ] **`Task 4`**: Enhance error handling
- [ ] **`Task 5`**: Add more advanced configuration options
- [ ] **`Task 6`**: Implement comprehensive logging

Enjoy the DailyMoodBoost experience! Stay hydrated, laugh more, get inspired, and never miss a match! 😊
