# Habit Tracker

This script is a habit tracker built using the Pixela API, which allows users to track their daily goals (like cycling, coding, or reading) in a GitHub-style intensity graph.

---

## ✨ Key Features

* **User Authentication:** Uses custom headers (X-USER-TOKEN) for secure API interaction.
* **Dynamic Date Handling:** Utilizes the datetime module to automatically format the current date as required by Pixela (YYYYMMDD).
* **Complete CRUD Capability** The code contains logic for:

***Create:*** Registering a new user and creating a tracking graph.
***Update:*** Modifying the quantity of a habit already logged for a specific day.

* **Customizable Metrics:** Configured for tracking cycling distance in kilometers (Km) with a specific color theme (ajisai).

---

## 🛠 Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **Libraries:** | requests, datetime, os |
| **API** | Pixela API |

---

## 🚀 Getting Started


Follow these step-by-step instructions to set up the tracker on your local machine.

### 1. Prerequisites
You will need a Pixela token. This acts as your password for the service.

### 2. Environment Variables
To keep your credentials secure, this script uses an environment variable for your token.

Create an environment variable named TOKEN.

Set its value to your chosen Pixela secret token.


### 3. Dependencies
Install the required requests library:

```bash
pip install requests
```

### 4. Execution
Run the orchestrator script to start tracking:

```bash
python main.py

```
## ⚙️ How It Works

The script follows the Pixela API lifecycle. While all configurations are present, the current execution is set to update a pixel.

### API Endpoints Used:

#### 1. User Creation:
[https://pixe.la/v1/users](https://pixe.la/v1/users)

#### 2. Graph Creation:
[https://pixe.la/v1/users/](https://pixe.la/v1/users/){username}/graphs

#### 3. Pixel Creation:
[https://pixe.la/v1/users/](https://pixe.la/v1/users/){username}/graphs/{graph_id}

#### 4. Pixel Update/Delete:
[https://pixe.la/v1/users/](https://pixe.la/v1/users/){username}/graphs/{graph_id}/{date}


## 📜 License

Proprietary. Developed as a python learning project. All rights reserved.