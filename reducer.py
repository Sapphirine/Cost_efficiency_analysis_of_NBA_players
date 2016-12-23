
import sys

current_player = None
sum_per = 0.0
sum_ows = 0.0
sum_dws = 0.0
sum_ws = 0.0
max_ows = 0.0
max_dws = 0.0
max_ws = 0.0
season = 0

for line in sys.stdin:
    line = line.strip()
    player, per, ows, dws, ws = line.split('\t', 4)

    try:
        per = float(per)
        ows = float(ows)
        dws = float(dws)
        ws = float(ws)
    except ValueError:
        continue

    if current_player == player:
        sum_per += per
        sum_ows += ows
        sum_dws += dws
        sum_ws += ws
        season += 1
        if max_ws < ws:
            max_ws = ws
            max_ows = ows
            max_dws = dws
    else:
        if current_player:
            aper = sum_per/season
            aows = sum_ows/season
            adws = sum_dws/season
            aws = sum_ws/season
            avg_per = float('%0.2f'%aper)
            avg_ows = float('%0.2f'%aows)
            avg_dws = float('%0.2f'%adws)
            avg_ws = float('%0.2f'%aws)
            print '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (current_player, avg_per, avg_ows, avg_dws, avg_ws, max_ows, max_dws, max_ws, season)
        current_player = player
        sum_per = per
        sum_ows = ows
        sum_dws = dws
        sum_ws = ws
        season = 1
        max_ows = ows
        max_dws = dws
        max_ws = ws

if current_player == player:
    aper = sum_per/season
    aows = sum_ows/season
    adws = sum_dws/season
    aws = sum_ws/season
    avg_per = float('%0.2f'%aper)
    avg_ows = float('%0.2f'%aows)
    avg_dws = float('%0.2f'%adws)
    avg_ws = float('%0.2f'%aws)
    print '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (current_player, avg_per, avg_ows, avg_dws, avg_ws, max_ows, max_dws, max_ws, season)
        