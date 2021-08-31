import urwid


REPLY = urwid.Text("")


def has_digits(pas):
    for sym in pas:
        if sym.isdigit():
            return True
    return False


def has_letters(pas):
    for sym in pas:
        if sym.isalpha():
            return True
    return False


def has_upper_letters(pas):
    for sym in pas:
        if sym.isupper():
            return True
    return False


def has_lower_letters(pas):
    for sym in pas:
        if sym.islower():
            return True
    return False


def is_long(pas):
    return len(pas) > 12


def has_symbols(pas):
    for sym in pas:
        if not sym.isdigit() and not sym.isalpha():
            return True
    return False


CRITERIONS = [
    has_digits, has_letters,
    has_upper_letters,
    has_lower_letters,
    is_long, has_symbols
]


def get_rating(pas):
    score = 0
    for function in CRITERIONS:
        if function(pas):
            score += 2
    return score


def on_ask_change(edit, pas):
    rating = get_rating(pas)
    REPLY.set_text("This password rating: {}".format(rating))


def main():
    ask = urwid.Edit("Insert password: ", mask="*")
    menu = urwid.Pile([ask, REPLY])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    main()
