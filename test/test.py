import pytest

from test.loadData import load_data

# За кровь из глаз заранее прошу прощения

@pytest.mark.parametrize("popularity",
                         [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
def test_popularity(popularity):
    sites = load_data()
    errors = []
    for site in sites:
        if site.Popularity < popularity:
            error = f"{site.Name} (Frontend:{site.Frontend}|Backend:{site.Backend}) has {site.Popularity} unique visitors per month. (Expected more than {popularity})"
            errors.append(error)
    assert not errors, "\n".join(errors)
