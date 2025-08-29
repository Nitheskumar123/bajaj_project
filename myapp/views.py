from django.shortcuts import render
import json, re
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def is_alpha_string(s):
    return isinstance(s, str) and s.isalpha()

def is_digit_string(s):
    return isinstance(s, str) and re.fullmatch(r'[0-9]+', s) is not None

def extract_all_letters(data):
    chars = []
    for item in data:
        if isinstance(item, str):
            for ch in item:
                if ch.isalpha():
                    chars.append(ch)
    return ''.join(chars)

def alternating_caps(s):
    out = []
    for i, ch in enumerate(s):
        if i % 2 == 0:
            out.append(ch.upper())
        else:
            out.append(ch.lower())
    return ''.join(out)


@csrf_exempt
def bfhl(request):
    if request.method == 'GET':
        # show a nice form in the browser
        return HttpResponse("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>BFHL API Test</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background: #f4f6f9;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .container {
                        background: white;
                        padding: 30px;
                        border-radius: 12px;
                        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                        width: 400px;
                        text-align: center;
                    }
                    h2 {
                        margin-bottom: 20px;
                        color: #333;
                    }
                    input[type=text] {
                        width: 90%;
                        padding: 10px;
                        margin: 10px 0;
                        border: 1px solid #ccc;
                        border-radius: 8px;
                        font-size: 14px;
                    }
                    input[type=submit] {
                        background: #007bff;
                        color: white;
                        border: none;
                        padding: 12px 20px;
                        font-size: 15px;
                        border-radius: 8px;
                        cursor: pointer;
                        transition: 0.3s;
                    }
                    input[type=submit]:hover {
                        background: #0056b3;
                    }
                    .footer {
                        margin-top: 15px;
                        font-size: 13px;
                        color: #666;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>BFHL API Test</h2>
                    <form method="post">
                        <label>Enter Data (comma separated):</label><br>
                        <input type="text" name="data" value="a,1,334,4,R,$"><br>
                        <input type="submit" value="Submit">
                    </form>
                    <div class="footer">POST request runs & shows JSON response here</div>
                </div>
            </body>
            </html>
        """)

    if request.method == 'POST':
        try:
            if request.content_type.startswith("application/x-www-form-urlencoded"):
                form_data = request.POST.get("data", "")
                data = [x.strip() for x in form_data.split(",")]
            else:
                payload = json.loads(request.body.decode('utf-8'))
                data = payload.get('data')
        except:
            return HttpResponseBadRequest('Invalid JSON')

        if not isinstance(data, list):
            return HttpResponseBadRequest('Invalid payload')

        even_numbers, odd_numbers, alphabets, special_characters = [], [], [], []
        total = 0

        for item in data:
            if is_digit_string(item):
                n = int(item)
                (even_numbers if n % 2 == 0 else odd_numbers).append(str(n))
                total += n
            elif is_alpha_string(item):
                alphabets.append(item.upper())
            elif isinstance(item, str):
                special_characters.append(item)

        letters = extract_all_letters(data)
        concat_string = alternating_caps(letters[::-1])

        response_data = {
            "is_success": True,
            "user_id": f"{settings.BFHL_FULL_NAME.lower()}_{settings.BFHL_DOB_DDMMYYYY}",
            "email": settings.BFHL_EMAIL,
            "roll_number": settings.BFHL_ROLL,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total),
            "concat_string": concat_string
        }

        # show JSON result in the browser
        return HttpResponse(
            f"<pre style='background:#1e1e1e;color:#dcdcdc;padding:20px;border-radius:8px;'>"
            f"{json.dumps(response_data, indent=4)}</pre>"
        )

    return HttpResponseBadRequest('Invalid method')

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bajaj Finance REST API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f9;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                text-align: center;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 20px;
                background: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: 0.3s;
            }
            a:hover {
                background: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Nithes Kumar S Bajaj Finance REST API Project</h1>
            <a href="/bfhl">Go to BFHL API</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

