import cider_ranking


def run():
    """
    Generate an HTML file
    """
    result = cider_ranking.list_ranking()
    with open("target.html", "w") as fh:
        fh.write(result)


if __name__ == '__main__':
    run()
