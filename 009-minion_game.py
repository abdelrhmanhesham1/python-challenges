Kevin and Stuart want to play the The Minion Game.

Game Rules
Both players are given the same string S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with wovels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example
String S = BANANA
Kevin's wovel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 points.

==>def minion_game(string):
    wovels = "AEIOU"
    x = 0
    y = 0

    for i in range(len(string)):
        if s[i] in wovels:
            x += len(string)-i
        else:
            y += len(string)-i

    if x > y:
        print("Kevin", x)
    elif x < y:
        print("Stuart", y)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
