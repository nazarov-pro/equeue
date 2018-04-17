from django.shortcuts import render
from django.http import FileResponse,HttpResponse, HttpResponseNotFound, HttpResponseForbidden
import datetime
from django.utils.timezone import now
import os, qrcode
from PIL import Image

# Create your views here.
def renderIndex(request):
    return HttpResponse('go go go')


# Create your views here.
def return_qr(request):
    text = request.GET.get('text')
    qr = generate_qr_code(text, 10, 4)
    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response

def renderIndex2(request):
    today = datetime.date.today()
    generate_qr_code(today).save('out.bmp')
    time = now()
    return render(request, 'equeue/index.html', {'name': 'Shahin',
                                          'today': today,
                                          'time' : time })

def generate_qr_code(data, size=10, border=0):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=size,
                       border=border)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color="#263238", back_color="#C5CAE9")