import datetime

def parse_content(content):
    updates = []
    deadlines = {}

    for i, line in enumerate(content):
        if "Added:" in line or "uploaded" in line.lower():
            updates.append(line.strip())
        if "Due Date:" in line:
            try:
                due_str = line.split("Due Date:")[1].strip()
                due_time = datetime.datetime.strptime(due_str, "%m/%d/%y, %I:%M %p (UTC+5:30)")
                title = content[i - 1] if i > 0 else f"Task-{i}"
                deadlines[title] = due_time
            except:
                pass
    return updates, deadlines