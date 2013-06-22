# Create your views here.


from qr.devices.models import Devices
from django.views.generic import DetailView
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy


class DetailDevice(DetailView):

    model = Devices
    template_name = "detail_device.html"
    context_object_name = "foo"



def get_qr_code(request, id):

    device = get_object_or_404(Devices, id = id)

    return render_to_response("qrcode.html", locals(),
                          context_instance = RequestContext(request))

