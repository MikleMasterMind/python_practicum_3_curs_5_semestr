packs = dict()
players = dict()
while s := input():
    s = s.split(' / ')
    if s[0].isnumeric():
        pack, card = s[0], s[1]
        # packs[pack] = packs.get(pack, 0) + 1
        if pack in packs:
            packs[pack].append(card)
        else:
            packs[pack] = [card]
    else:
        player, pack = s[0], s[1]
        if player in players:
            players[player].append(pack)
        else:
            players[player] = [pack]
count_card = dict()
mx = 0
for player in players: 
    card_num = {i for pack in players[player] for i in packs[pack]}
    count_card[player] = len(card_num)
    mx = max(mx, len(card_num))
ans = [player for player in count_card if count_card[player] == mx]
print(*sorted(ans), sep='\n')