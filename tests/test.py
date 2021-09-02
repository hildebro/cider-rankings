import cider_ranking


def run():
    """
    Generate an HTML file
    """
    # Only required once, but doesn't hurt to execute on every run
    cider_ranking.init_db()

    result = cider_ranking.list_ranking()
    for cider in result:
        print(cider)


if __name__ == '__main__':
    run()
