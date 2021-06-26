import youtube_dl
import os
import re

TECHS = ['react', 'node', 'elixir', 'flutter', 'reactnative']
EDICAO = 6

path = os.getcwd()
for tech in TECHS:
    os.chdir(path)

    # path

    # check if path exists
    if(not os.path.exists(tech)):
        print(f'[{tech}] Creating folder...')
        os.mkdir(tech)
    os.chdir(f'{path}/{tech}')

    # download videos
    with youtube_dl.YoutubeDL({}) as yt:
        # download episodes 1 -> 5
        for episode in range(1,6):
            video_url = f'https://nextlevelweek.com/episodios/{tech}/aula-{episode}/edicao/{EDICAO}'

            # check if episode is already downloades
            if(re.search(f'Aula 0{episode}', "".join(os.listdir(".")))):
                print(f'[{tech}] Episode {episode} already downloaded, skipping...')
                continue

            # youtube download
            print(f'[{tech}] Downloading Aula 0{episode} ({video_url})')
            yt.download([video_url])
