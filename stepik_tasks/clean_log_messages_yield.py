def clean_log_messages(log_lines):
    for log_line in log_lines:
        if "ERROR" in log_line:
            yield log_line.strip()
raw_logs = [
    "  [2026-10-13 14:00:00] [INFO] Server started successfully  ",
    "[2026-10-13 14:05:12] [ERROR] Database connection failed",
    "   [2026-10-13 14:10:30] [WARNING] High memory usage   ",
    "[2026-10-13 14:15:45] [ERROR] Timeout while waiting for response"
]

for cleaned_log in clean_log_messages(raw_logs):
    print(cleaned_log)