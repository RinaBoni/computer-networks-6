import subprocess
import psutil

print('Запустить udp или tcp чат?')
answer = input()


if answer == 'udp':
    subprocess.run(['py', './UDP/client.py'])


if answer == 'tcp':
    subprocess.run(['py', './TCP/client.py'])

# def is_python_script_running(script_name):
#     for process in psutil.process_iter(['name', 'py', 'cmdline']):
#         try:
#             if process.info['name'] == 'python.py' and script_name in process.info['cmdline']:
#                 return True
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#     return False
#
#
# print('Запустить udp или tcp чат?')
# answer = input()
#
#
# if answer == 'udp':
#     if is_python_script_running('./UDP/server.py'):
#         subprocess.run(['py', './UDP/client.py'])
#     else:
#         subprocess.Popen(['py', './UDP/server.py'], stdout=subprocess.DEVNULL)
#         subprocess.run(['py', './UDP/client.py'])
#
#
# if answer == 'tcp':
#     if is_python_script_running('./TCP/server.py'):
#         subprocess.run(['py', './TCP/client.py'])
#     else:
#         subprocess.Popen(['py', './TCP/server.py'], stdout=subprocess.DEVNULL)
#         subprocess.run(['py', './TCP/client.py'])
