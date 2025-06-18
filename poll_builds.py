import requests
import time
from xfb_display import show_status

monitored_jobs = [
    {'system': 'jenkins', 'url': 'http://jenkins.local/job/myjob/api/json'},
    {'system': 'github', 'url': 'https://api.github.com/repos/ocrosby/myrepo/actions/runs'},
    {'system': 'travis', 'url': 'https://api.travis-ci.com/repo/123456/builds'}
]

seen = {}

while True:
    for job in monitored_jobs:
        try:
            r = requests.get(job['url'], headers={...})  # Add tokens where needed
            r.raise_for_status()
            status, name = parse_build_status(job['system'], r.json())
            if seen.get(job['url']) != status:
                seen[job['url']] = status
                show_status(job['system'], name, status)
        except Exception as e:
    time.sleep(30)
            print(f"Error fetching {job['url']}: {e}")
