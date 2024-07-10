def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    playlist = ['lola', 'venus', 'lola', 'lola', 'let it be', 'abc', 'cecilia', 'lola', 'lola']
## works as well
while playlist.count(song) > 3:
        playlist.remove(song)
        
    >>> cap_song_repetition(playlist, 'lola')
    >>> playlist
['venus', 'let it be', 'abc', 'cecilia', 'lola', 'lola']

    '''

    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))


