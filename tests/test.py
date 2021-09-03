import cider_ranking


def run():
    """
    Generate an HTML file
    """
    # Only required once, but doesn't hurt to execute on every run
    cider_ranking.init_db()

    if not cider_ranking.has_ranking('Sommersby'):
        cider_ranking.add_ranking('Sommersby', 5, 1, 4)
    if not cider_ranking.has_ranking('Rekorderlig'):
        cider_ranking.add_ranking('Rekorderlig', 3, 2, 4)
    if not cider_ranking.has_ranking('Räuber'):
        cider_ranking.add_ranking('Räuber', 1, 5, 5)
    if not cider_ranking.has_ranking('Lies!'):
        cider_ranking.add_ranking('Lies!', 4, 2, 1)

    result = cider_ranking.get_all()
    for cider in result:
        print(cider)


if __name__ == '__main__':
    run()
