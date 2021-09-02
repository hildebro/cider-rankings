import cider_ranking


def run():
    """
    Generate an HTML file
    """
    # Only required once, but doesn't hurt to execute on every run
    cider_ranking.init_db()

    if not cider_ranking.has_ranking('Sommersby'):
        cider_ranking.add_ranking('Sommersby', 5, 1, 4)

    result = cider_ranking.get_all()
    for cider in result:
        print(cider)


if __name__ == '__main__':
    run()
