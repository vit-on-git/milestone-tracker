# milestone-tracker
Personal Milestone Tracker: A Streamlit app to track birthdays, death days, and anniversaries. Upload an Excel file, filter by month, and download results as CSV. Perfect for organizing important dates! 🗓️📤📥

# Personal Milestone Tracker

A Streamlit app to track personal milestones such as birthdays, death days, and anniversaries. The app allows users to upload an Excel file, filter milestones by month, and download the filtered results as a CSV file.

## Features
- **Upload Excel File**: Users can upload an Excel file containing milestone data.
- **Filter by Month**: The app filters milestones (birthdays, death days, anniversaries) for a specific month.
- **Download Results**: Users can download the filtered results as a CSV file.
- **UTF-8 Support**: The app ensures proper handling of non-ASCII characters (e.g., Russian text) in the CSV file.

## How to Use
1. **Upload an Excel File**:
   - The Excel file should have columns named `BirthDay`, `DeathDay`, and `Anniversary` (case-sensitive).
   - Dates should be in a valid format (e.g., `YYYY-MM-DD`).

2. **Select a Sheet**:
   - If the Excel file contains multiple sheets, select the sheet you want to analyze.

3. **Filter by Month**:
   - Enter a month (1-12) to filter milestones for that month.

4. **Download Results**:
   - The app will display the filtered milestones and allow you to download them as a CSV file.

## Run the App Locally
To run the app locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/milestone-tracker.git
   cd milestone-tracker
