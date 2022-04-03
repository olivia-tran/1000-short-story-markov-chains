import markovify

with open('grimm_tales.txt') as f:
    text = f.read()
with open('little_red_riding_hood.txt') as f:
    text += f.read()
with open('robin_hood_prologue.txt') as f:
    text += f.read()

text_model = markovify.Text(text)
short_story = ''

while len(short_story.split(" ")) < 1000:
    for i in range(2):
        short_story += text_model.make_sentence()

print(short_story)
