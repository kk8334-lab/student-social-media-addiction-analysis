# Social Media Addiction Dashboard

A Django web application that analyzes and visualizes student social media addiction patterns using interactive charts and data analytics.

## Features

- Interactive data visualizations using Plotly
-  Filter data by gender and platform
-  Four comprehensive charts:
  - Average Daily Usage by Platform
  - Addiction Score Distribution by Gender
  - Sleep Hours vs Mental Health Score
  - Country-wise Average Addiction Score
-  Dataset preview with first 10 rows
-  Responsive design with clean UI

## Technologies Used

- *Backend*: Django 5.2.7
- *Data Processing*: Pandas 2.3.3
- *Visualizations*: Plotly 6.4.0
- *Database*: SQLite3
- *Python*: 3.13+

---

## Windows Setup Instructions (Step-by-Step)

### Prerequisites

Before you begin, make sure you have:
- *Python 3.10 or higher* installed on your Windows machine
- *Git* installed (download from [git-scm.com](https://git-scm.com/))
- *Command Prompt* or *PowerShell* access

---

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, *check the box "Add Python to PATH"*
3. Verify installation by opening *Command Prompt* and running:
   bash
   python --version
   
   You should see something like Python 3.13.x

---

### Step 2: Clone the Repository

1. Open *Command Prompt* or *PowerShell*
2. Navigate to where you want to store the project:
   bash
   cd C:\Users\YourUsername\Documents
   
3. Clone the repository:
   bash
   
4. Navigate into the project folder:
   bash
   cd Social-media-addiction\social_addiction
   

---

### Step 3: Create a Virtual Environment

1. Create a virtual environment:
   bash
   python -m venv env
   
2. Activate the virtual environment:
   bash
   env\Scripts\activate
   
   
   *Note*: If you see an error about execution policies, run PowerShell as Administrator and execute:
   powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   
   Then try activating again.

3. You should see (env) appear at the beginning of your command prompt line.

---

### Step 4: Install Dependencies

With the virtual environment activated, install all required packages:

bash
pip install -r requirements.txt


This will install:
- Django
- pandas
- plotly
- numpy
- and all other dependencies

---

### Step 5: Set Up the Database

Run Django migrations to set up the SQLite database:

bash
python manage.py migrate


---

### Step 6: Run the Development Server

Start the Django development server:

bash
python manage.py runserver


You should see output like:

Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


---

### Step 7: Access the Dashboard

1. Open your web browser
2. Go to: *http://127.0.0.1:8000/* or *http://localhost:8000/*
3. You should see the Social Media Addiction Dashboard!

---

## Using the Dashboard

1. *Filter Data*: Use the dropdown menus to filter by:
   - Gender (Male/Female/All)
   - Platform (Instagram/Facebook/Twitter/etc./All)

2. *View Statistics*: Four summary cards show:
   - Average Addiction Score
   - Average Daily Usage Hours
   - Average Sleep Hours
   - Average Mental Health Score

3. *Dataset Preview*: See the first 10 rows of filtered data in a table

4. *Interactive Charts*: Scroll down to view four interactive Plotly charts

---

## Troubleshooting

### Issue: "python is not recognized"
*Solution*: Python is not in your PATH. Reinstall Python and check "Add Python to PATH" during installation.

### Issue: "pip is not recognized"
*Solution*: Try using python -m pip instead of pip:
bash
python -m pip install -r requirements.txt


### Issue: Virtual environment won't activate
*Solution*: If using PowerShell, you may need to change the execution policy (see Step 3).

### Issue: Port 8000 already in use
*Solution*: Either:
- Stop the other process using port 8000, or
- Run on a different port:
  bash
  python manage.py runserver 8001
  

### Issue: Missing CSV file error
*Solution*: Make sure the dataset file exists at:

dashboard/static/dataset/Students Social Media Addiction.csv


---

## Project Structure


<img width="547" height="514" alt="image" src="https://github.com/user-attachments/assets/63db56ef-7dff-4fe4-a4b1-b1a2d0caf3b7" />


---

## Stopping the Server

To stop the development server:
- Press *CTRL + C* in the Command Prompt/PowerShell window

To deactivate the virtual environment:
bash
deactivate


---

## Notes

- This is a *development server* - not suitable for production
- The dataset is included in the repository
- No database migrations needed (no models defined)
- All data processing happens on-the-fly using pandas

---

## Future Enhancements

- [ ] Add data upload functionality
- [ ] Export filtered data to CSV
- [ ] User authentication
- [ ] Save favorite filter combinations
- [ ] Add more visualization options
- [ ] Implement caching for better performance

---

## License

This project is open source and available for educational purposes.
## Quick Reference Commands

bash
# Clone repository
cd Social-media-addiction\social_addiction

# Set up environment
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver

# Access dashboard
# Open browser to: http://127.0.0.1:8000/
**#OUTPUT**
<img width="1880" height="893" alt="image" src="https://github.com/user-attachments/assets/d1f38658-3359-47c2-b72e-d93683395f50" />
<img width="1844" height="783" alt="image" src="https://github.com/user-attachments/assets/2f464818-b44b-4020-b43a-6101bd6181bd" />
<img width="1815" height="687" alt="image" src="https://github.com/user-attachments/assets/fcad6c45-9bd7-49b6-bdeb-e64ff6348698" />
<img width="1848" height="696" alt="image" src="https://github.com/user-attachments/assets/63d6560c-0d38-44fa-bd02-c82381f53378" />
<img width="1785" height="610" alt="image" src="https://github.com/user-attachments/assets/270eac35-2bf5-44df-8ede-15128f36b40e" />





