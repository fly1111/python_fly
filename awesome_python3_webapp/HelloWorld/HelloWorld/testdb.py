from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
    response = ""
    response1 = ""
    #通过obects模型的all（）获得所有数据行相当于selest *frem
    list1 = Test.objects.all()
    #filter x相当于where
    response2 = Test.objects.filter(id=1)
    response3 = Test.objects.get(id = 1)
    Test.objects.order_by('name')[0:2]
    Test.objects.order_by("id")
    Test.objects.filter(name = 'message').order_by("id")
    for var in list1:
        response1 += var.name +" "
        response = response1
        return HttpResponse("<p>"+response+"</p>")

    
