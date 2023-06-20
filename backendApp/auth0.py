# # 📁 server.py -----
# import os
# import json
# from os import environ as env
# from urllib.parse import quote_plus, urlencode

# from authlib.integrations.flask_client import OAuth
# from dotenv import find_dotenv, load_dotenv
# from flask import Flask, redirect, render_template, session, url_for

# # 👆 We're continuing from the steps above. Append this to your server.py file.

# secret_key = os.urandom(24).hex()
# ENV_FILE = find_dotenv()
# if ENV_FILE:
#     load_dotenv(ENV_FILE)
# # 👆 We're continuing from the steps above. Append this to your server.py file.

# app = Flask(__name__)
# app.secret_key = secret_key

# # 👆 We're continuing from the steps above. Append this to your server.py file.

# oauth = OAuth(app)

# oauth.register(
#     "auth0",
#     client_id=env.get("AUTH0_CLIENT_ID"),
#     client_secret=secret_key,
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
# )

# # 👆 We're continuing from the steps above. Append this to your server.py file.

# @app.route("/login")
# def login():
#     return oauth.auth0.authorize_redirect(
#         redirect_uri=url_for("callback", _external=True)
#     )
# # 👆 We're continuing from the steps above. Append this to your server.py file.

# @app.route("/callback", methods=["GET", "POST"])
# def callback():
#     token = oauth.auth0.authorize_access_token()
#     session["user"] = token
#     return redirect("/")
# # 👆 We're continuing from the steps above. Append this to your server.py file.

# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(
#         "https://" + env.get("AUTH0_DOMAIN")
#         + "/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": url_for("home", _external=True),
#                 "client_id": env.get("AUTH0_CLIENT_ID"),
#             },
#             quote_via=quote_plus,
#         )
#     )
# # 👆 We're continuing from the steps above. Append this to your server.py file.

# @app.route("/")
# def home():
#     return render_template("home.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

# # 👆 We're continuing from the steps above. Append this to your server.py file.

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=env.get("PORT", 5000));

import os

from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, session, jsonify,url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Pour autoriser les requêtes CORS

secret_key = os.urandom(24).hex()
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app.secret_key = secret_key
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=secret_key,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
       redirect_uri=url_for("get_auth_user", _external=True)  # Remplacez par votre URL de redirection
    )

# @app.route("/callback")
# def callback():
#     token = oauth.auth0.authorize_access_token()
#     session["user"] = token
#     return redirect("http://localhost:5000/home")  # Remplacez par votre URL de redirection après la connexion

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": "http://localhost:5000",  # Remplacez par votre URL de redirection après la déconnexion
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@app.route("/user")
def get_user():
    user = session.get("user")
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not authenticated"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
