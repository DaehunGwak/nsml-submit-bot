import os
import sys
import time
import subprocess
from multiprocessing import Process
from datetime import datetime

###########################################################################################
"""
이 아래의 Variables에 자기가 제출할 타이밍과
팀명, 데이터 셋 이름, 세션 이름 들, 모델 이름 들을 넣어주면 됩니다.
sessions와 models 사이즈는 일치 시켜주시길 바라며,
각 제출은 처음 start_wait_sec만큼 기다린 다음
한 시간 단위마다 제출합니다.
"""
team_name = "team_41"       # 팀 이름을 넣어주시면 됩니다.
data_name = "ir_ph2"        # 데이터 셋 이름을 넣어주시면 됩니다.
sessions = ['401', '402']   # 세션 번호를 문자열로 넣어주시면 됩니다.
models = ['1', '1']         # 모델 이름을 넣어주면 됩니다.
start_wait_sec = 3          # 해당 초만큼 기다린 다음 submit command를 실행합니다
###########################################################################################


def run_submit(command):
    now = time.time()
    print(f"[Command] {command}")
    print(datetime.now())
    subprocess.call(command)
    print(f"[Collapsed time] {time.time() - now}")


if __name__ == "__main__":
    S_HOUR = 3601
    li_procs = []

    for s, m in zip(sessions, models):
        full_session = '/'.join([team_name, data_name, s])
        full_command = f"nsml submit {full_session} {m}"
        li_procs.append(Process(target=run_submit, args=(full_command, )))

    now = time.time()
    time.sleep(start_wait_sec)

    for i, proc in enumerate(li_procs):
        proc.start()
        if i + 1 < len(li_procs):
            time.sleep(S_HOUR)

    for proc in li_procs:
        proc.join()
    print(f"Total collapsed time: {time.time() - now}")
