# You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

import jwt

METABASE_SITE_URL = "http://10.0.100.210:3000"
METABASE_SECRET_KEY = "a9356a127ec6120c15c3c0f108c762071a42cfd63540c133361aa5065d88683e"

payload = {
    "resource": {"dashboard": 1},
    "params": {

    }
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token.decode("utf8") + "#bordered=true&titled=true"