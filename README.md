# DailyMoodBoost

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
    ├── config.py
    ├── database
    │   └── extension.py
    ├── external_api
    │   ├── __init__.py.py
    │   └── jokes.py
    ├── main.py
    ├── requirements.txt
    ├── schemas
    │   ├── jokes_schema.py
    │   └── message_schema.py
    ├── sms_manager.py
    └── sqlite_manager.py
```

### 📂 Project Index
<details open>
	<summary><b><code>HACKATHON-GROUP-1/</code></b></summary>
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b>sqlite_manager.py</b></td>
				<td>Manages SQLite database interactions and queries</td>
			</tr>
			<tr>
				<td><b>config.py</b></td>
				<td>Centralized configuration settings for the application</td>
			</tr>
			<tr>
				<td><b>main.py</b></td>
				<td>Primary entry point for the application</td>
			</tr>
			<tr>
				<td><b>requirements.txt</b></td>
				<td>Lists all Python package dependencies</td>
			</tr>
			<tr>
				<td><b>sms_manager.py</b></td>
				<td>Handles SMS sending and related functionalities</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details>
		<summary><b>schemas</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b>message_schema.py</b></td>
				<td>Defines data models for message-related structures</td>
			</tr>
			<tr>
				<td><b>jokes_schema.py</b></td>
				<td>Provides data models for joke-related content</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details>
		<summary><b>external_api</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b>jokes.py</b></td>
				<td>Interfaces with external joke APIs to fetch random jokes</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details>
		<summary><b>database</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b>extension.py</b></td>
				<td>Provides additional database-related utilities</td>
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