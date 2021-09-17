from starlette.testclient import TestClient
from sql_app import schemas, models, crud
from sql_app.database import orm_connection

# SessionLocal, engine = orm_connection()
# models.Base.metadata.create_all(bind=engine)

# db = SessionLocal()
# # # Dependency
# # def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_landing(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"title": "Backend API for the wedding project"}

def test_login_existing(test_app):
    response = test_app.get("/login/3002022460")
    assert response.status_code == 200
    assert response.json() == {'attendance_confirmation': 'False', \
                               'family_name': 'Familia Tovar Uribe', \
                               'Number of assistants': '2'} 

def test_login_unexisting(test_app):
    response = test_app.get("/login/6692958490")
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}  

def test_attendance_confirmation(test_app):
    response = test_app.put(
        "/confirmation/3002022460",
        
        json={
                "attendance_confirmation": "false"
        }
    )
    assert response.status_code == 200
    assert response.json() == [{
        "guest_id": 21,
        "family_id": 11,
        "name": "Juan Jose Tovar",
        "phone_number": "3002022460",
        "attendance_confirmation": 0,
        "allergies": "",
        "additional_comments": ""},
        {"guest_id": 22,
        "name": "Sylvia Uribe",
        "attendance_confirmation": 0,
        "additional_comments": "",
        "family_id": 11,
        "phone_number": "6693015868",
        "allergies": ""
    }]


# def test_family_members():
#     assert crud.get_family_members(db, phone_number)

# # def test_login():
# #     response = cliend.post("/login")
# #     assert response.status_code == 200
#     # assert response.json() == 