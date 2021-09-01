from jinja2 import Environment, PackageLoader, select_autoescape


def list_ranking():
    env = Environment(
        loader=PackageLoader('cider_ranking', 'templates'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('template.html')
    return template.render()
