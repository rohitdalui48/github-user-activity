
# GitHub User Activity CLI

A lightweight Command Line Interface (CLI) application that fetches and displays the recent public activity of any GitHub user directly in the terminal using the GitHub API.

This project was built as part of the roadmap.sh project-based learning path.

🔗 **Project URL:** [https://roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity)

---

## 📌 Features

* Accepts a GitHub username as a command-line argument
* Fetches recent public activity using the GitHub API
* Displays activity in a clean and readable terminal format
* Supports multiple GitHub event types such as:

  * Push events
  * Issues opened
  * Pull requests
  * Repository stars
  * Fork events
* Graceful error handling for:

  * Invalid usernames
  * API failures
  * Network issues
  * No activity found

---

## 🛠️ Tech Stack

* **Language:** Python
* **API:** GitHub REST API
* **Interface:** Command Line / Terminal

---

## 📂 Project Structure

```bash
github-user-activity/
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://rohitdalui48/github-user-activity
cd github-user-activity
```

### Run the Application

```bash
python main.py <github-username>
```

### Example

```bash
python main.py kamranahmedse
```

---

## 🖥️ Sample Output

```bash
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- Created a pull request in kamranahmedse/developer-roadmap
```

---

## 🌐 API Endpoint Used

```bash
https://api.github.com/users/<username>/events
```

Example:

```bash
https://api.github.com/users/kamranahmedse/events
```

## 👨‍💻 Author

**Rohit Dalui**
