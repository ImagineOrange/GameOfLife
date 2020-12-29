import pandas as pd

url = 'https://meyer-projects.com/Particles/particles.html'

dfs = pd.read_html(url)

print(len(dfs))

print(dfs[0])
