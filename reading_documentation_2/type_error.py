# The following code raises a TypeError:
# TypeError: can only concatenate str (not "int") to str

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

# length_of_tweet = len(tweet + 5) can not concatenate str and int

length_of_tweet = (len(tweet) + 5) # can use () to separate the str and int
print(length_of_tweet)
