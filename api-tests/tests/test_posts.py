def test_get_post_returns_200(api):
    response = api.get(f'{api.base_url}/posts/1')
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_post(api):
    playload = {"title": "x", "body": "y", "userId": 1}
    response = api.post(f'{api.base_url}/posts', json=playload)
    assert response.status_code == 201
    assert response.json()["title"] == "x"

def test_missing_post_returns_404(api):
    assert api.get(f'{api.base_url}/posts/99999').status_code == 404
