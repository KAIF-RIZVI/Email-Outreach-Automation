# Email Outreach Automation

A Python-based email outreach automation system for sending personalized emails using dynamic templates, Excel contact management, and Gmail SMTP.

> Designed to automate repetitive outreach workflows while maintaining personalized communication at scale.

---

## Features

- Dynamic email personalization
- Excel-based contact management
- Customizable email templates
- Dynamic subject generation
- Gmail SMTP integration
- PDF attachment support
- Duplicate email detection
- Batch email processing
- Configurable sending intervals
- Real-time progress tracking
- Exception handling

---

## Tech Stack

- Python
- Pandas
- OpenPyXL
- Gmail SMTP
- EmailMessage
- File Handling
- Excel Processing

---

## Project Structure

```text
Email-Outreach-Automation/
│
├── send.py
├── email_template.txt
├── sample_emails.xlsx
├── sample_resume.pdf
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Input Format

The application expects an Excel file with the following columns:

| Name | Company | Email | Role |
|------|----------|-------|------|

### Example

| John Doe | ABC Technologies | john@abc.com | HR |

---

## Supported Template Variables

```text
{name}
{company}
{role}
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/KAIF-RIZVI/Email-Outreach-Automation.git
```

Move into the project:

```bash
cd Email-Outreach-Automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

For security, the application loads credentials from a `.env` file instead of hardcoding them in `send.py`.

1. Copy the template to create a `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Configure your credentials and sender name in `.env`:
   ```env
   EMAIL=your_email@gmail.com
   APP_PASSWORD=your_16_character_app_password
   SENDER_NAME=Your Name
   ```
3. Run the script:
   ```bash
   python send.py
   ```

---

## Workflow

```text
Excel Contacts
      │
      ▼
Read Dataset
      │
      ▼
Render Template
      │
      ▼
Attach Resume
      │
      ▼
Authenticate via Gmail SMTP
      │
      ▼
Send Email
      │
      ▼
Progress Tracking
```

---

## Roadmap

- HTML email templates
- Email scheduling
- Multi-account SMTP support
- Delivery logging
- Resume interrupted campaigns
- GUI dashboard
- Contact segmentation
- Analytics & reporting

---

## Disclaimer

This project is intended for legitimate professional communication and educational purposes. Users are responsible for complying with applicable laws, recipient preferences, and email provider policies.

---

## Author

**MOHD KAIF**

GitHub  
https://github.com/KAIF-RIZVI

LinkedIn  
https://www.linkedin.com/in/mohdkaifrizvi
