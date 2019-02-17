import os
import sys
import time
import subprocess
from multiprocessing import Process
from datetime import datetime

team_name = "team_41"
data_name = "ir_ph2"
sessions = ['381', '401', '402']
models = ['21', '1', '1']


def run_submit(command):
    now = time.time()
    print(f"[Command] {command}")
    print(datetime.now())
    # subprocess.call(command)
    print(f"[Collapsed time] {time.time() - now}")


if __name__ == "__main__":
    S_HOUR = 5 # 3600
    li_procs = []

    for s, m in zip(sessions, models):
        full_session = '/'.join([team_name, data_name, s])
        full_command = f"nsml submit {full_session} {m}"
        li_procs.append(Process(target=run_submit, args=(full_command, )))

    now = time.time()
    for proc in li_procs:
        time.sleep(S_HOUR)
        proc.start()
    for proc in li_procs:
        proc.join()
    print(f"Total collapsed time: {time.time() - now}")
