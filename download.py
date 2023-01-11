import requests
import os
import threading
import queue

headers = {'user-agent': '123456',
            'sec-fetch-dest': 'emplty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'accept-encoding': 'gzip, deflate, br',
            'origin' : 'https://123456',
            'referer' : 'https://123456/'}

def download(episode, num, queue):
    episode_0 = episode.rjust(3, '0')
    num_0 = num.rjust(3, '0')
    # print(episode, num)
    url = 'omg' 
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        print(url)
        with open(f'./{episode}/{num}.ts', 'wb') as f:
            f.write(response.content)
    queue.get()

if __name__ == '__main__':
    for ep in range(1, 26):
        if not os.path.exists(str(ep)):
            os.makedirs(str(ep))
        # max worker = 8
        thread_q = queue.Queue(maxsize=8)
        threads = []
        for num in range(0, 151):
            thread_q.put(1)
            thread = threading.Thread(target=download, args=(str(ep), str(num), thread_q))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
            
