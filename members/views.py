import qrcode
from django.http import HttpResponse
from io import BytesIO


def member_qr(request, uuid):

    qr = qrcode.make(uuid)

    buffer = BytesIO()
    qr.save(buffer)

    return HttpResponse(
        buffer.getvalue(),
        content_type="image/png"
    )