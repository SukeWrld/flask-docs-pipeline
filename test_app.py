from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert "¡Hola desde Flask con Jenkins!" in response.get_data(as_text=True)
