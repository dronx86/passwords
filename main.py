import urwid


def has_digits(pas):
    return any(sym.isdigit() for sym in pas)


def has_letters(pas):
    return any(sym.isalpha() for sym in pas)


def has_upper_letters(pas):
    return any(sym.isupper() for sym in pas)


def has_lower_letters(pas):
    return any(sym.islower() for sym in pas)


def is_long(pas):
    return len(pas) > 12


def has_symbols(pas):
    return any(not (sym.isdigit() or sym.isalpha()) for sym in pas)


def get_rating(pas):
    score = 0
    for function in criterions:
        if function(pas):
            score += 2
    return score


def on_ask_change(edit, pas):
    rating = get_rating(pas)
    reply.set_text("This password rating: {}".format(rating))


def main():
    
    global criterions, reply

    criterions = [
    has_digits, has_letters,
    has_upper_letters,
    has_lower_letters,
    is_long, has_symbols
    ]
    
    reply = urwid.Text("")
    ask = urwid.Edit("Insert password: ", mask="*")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    main()
