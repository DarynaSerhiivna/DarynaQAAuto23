import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt' 


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'] [0] ['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0 



@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emoji_unicorn_link_is_correct(github_api):
    r = github_api.get_emojis()
    assert r['unicorn'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f984.png?v8'   


@pytest.mark.api
def test_total_emoji_count(github_api):
    r = github_api.get_emojis()
    assert len(r) == 1877


@pytest.mark.api
def test_total_commits_count_on_default_branch(github_api):
    r = github_api.list_commits('DarynaSerhiivna')
    assert len(r) == 11


@pytest.mark.api
def test_wrong_repos_owner_name(github_api):
    r =  github_api.list_commits('Daryna')
    assert r['message']  == 'Not Found'