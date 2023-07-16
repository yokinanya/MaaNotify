import re
from notify import handle_notify


def find_last_start_up(items):
    last_start_up_index = -1
    for index, item in reversed(list(enumerate(items))):
        if "开始任务: StartUp" in item:
            last_start_up_index = index
            break
    if last_start_up_index != -1:
        return items[last_start_up_index:]
    else:
        return []


with open("debug/gui.log", "r", encoding="utf8") as _logs:
    logs = _logs.readlines()
logs_msg = []
for items in logs:
    match = re.match(r"\[(.*)\] <.*> (.*)", items)
    if match:
        time = match.group(1)
        message = match.group(2)
        logs_msg.append(message)
    else:
        logs_msg.append(items.replace('\n', '').replace('\r', ''))
last_logs = find_last_start_up(logs_msg)
content = "  \n".join(last_logs)
print(content)
# handle_notify(title=f"MAA Notify", content=content)
