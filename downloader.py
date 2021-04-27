from __future__ import unicode_literals
import youtube_dl
import os

techs = ['react', 'node', 'elixir', 'flutter', 'reactnative']
episode = 1

# React

# os.mkdir('react')
path = os.getcwd()
# os.chdir(f'{path}/react')

# for episode in range(1, 6, 1):
#     ytOptions = {}
#     with youtube_dl.YoutubeDL(ytOptions) as yt:
#         yt.download([f'https://nextlevelweek.com/episodios/{techs[0]}/{episode}/edicao/5'])
#         episode += 1

# # NodeJS

# os.chdir(f'{path}')
# os.mkdir('node')
# os.chdir(f'{path}/node')

# for episode in range(1, 6, 1):
#     ytOptions = {}
#     with youtube_dl.YoutubeDL(ytOptions) as yt:
#         yt.download([f'https://nextlevelweek.com/episodios/{techs[1]}/{episode}/edicao/5'])
#         episode += 1

# # Elixir

# os.chdir(f'{path}')
# os.mkdir('elixir')
# os.chdir(f'{path}/elixir')

# for episode in range(1, 6, 1):
#     ytOptions = {}
#     with youtube_dl.YoutubeDL(ytOptions) as yt:
#         yt.download([f'https://nextlevelweek.com/episodios/{techs[2]}/{episode}/edicao/5'])
#         episode += 1

# # Flutter

# os.chdir(f'{path}')
# os.mkdir('flutter')
# os.chdir(f'{path}/flutter')

# for episode in range(1, 6, 1):
#     ytOptions = {}
#     with youtube_dl.YoutubeDL(ytOptions) as yt:
#         yt.download([f'https://nextlevelweek.com/episodios/{techs[3]}/{episode}/edicao/5'])
#         episode += 1

# React Native

os.chdir(f'{path}')
os.mkdir('react-native')
os.chdir(f'{path}/react-native')

for episode in range(1, 6, 1):
    ytOptions = {}
    with youtube_dl.YoutubeDL(ytOptions) as yt:
        yt.download([f'https://nextlevelweek.com/episodios/{techs[4]}/{episode}/edicao/5'])
        episode += 1


