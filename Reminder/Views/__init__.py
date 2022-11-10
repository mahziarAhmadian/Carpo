from django.http import JsonResponse


def result_creator(status="ok", code=200, data=None, farsi_message="با موفقیت انجام شد.",
                   english_message="successfully done."):
    result = {
        "status": status,
        "code": code,
        "data": data,
        "farsi_message": farsi_message,
        "english_message": english_message
    }
    response = JsonResponse(result, status=result["code"], safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response
