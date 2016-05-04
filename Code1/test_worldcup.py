import nose.tools as n
import worldcup


def get_message(result, expected):
    message = 'Incorrect result. You returned\n{0}\ninstead of\n{1}'
    return message.format(result, expected)


def test_read_game_info():
    actual = worldcup.read_game_info('data/worldcup/1-1.txt')
    expected = ('22 MAR 2015 - 19:00', 'Barbados', 'US Virgin Islands', 0, 1)
    n.assert_equal(expected, actual, get_message(actual, expected))


def test_display_game():
    time = '22 MAR 2015 - 19:00'
    team = 'Barbados'
    other = 'US Virgin Islands'
    team_score = 0
    other_score = 1
    actual = worldcup.display_game(time, team, other, team_score, other_score)
    expected1 = '22 MAR 2015 - 19:00: Barbados (0) - US Virgin Islands (1)'
    expected2 = 'Mar 22: Barbados (0) - US Virgin Islands (1)'
    n.assert_true(expected1 == actual or expected2 == actual,
                  get_message(actual, expected1))


def test_display_summary():
    team = 'A'
    data = [('22 MAR 2015 - 19:00', 'A', 'B', 1, 0),
            ('23 MAR 2015 - 19:00', 'A', 'C', 1, 3),
            ('24 MAR 2015 - 19:00', 'C', 'B', 0, 0),
            ('25 MAR 2015 - 19:00', 'C', 'A', 2, 2),
            ('26 MAR 2015 - 19:00', 'A', 'D', 2, 1)]
    actual = worldcup.display_summary(team, data, detailed=False)
    expected = 'A played a total of 4 games.\n' \
               '2 win(s), 1 loss(es), 1 tie(s), 6 total goal(s)'
    n.assert_equal(expected, actual, get_message(actual, expected))
