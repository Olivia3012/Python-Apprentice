"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧.', 'and', 'went.', 'had', 'play', '⚽', 'they']

story = []
for i in (0,2,7,9,1,14,13,5,6,7,18,14,3,14,12,10,17):
    story.append(words[i])

# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))