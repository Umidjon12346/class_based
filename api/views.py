from django.http import HttpRequest, JsonResponse
from django.views import View
from .models import Smartphones
import json
import random



def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'url': self.img_url,
            'color': self.color,
            'ram': self.ram,
            'memory': self.memory,
            'name': self.name,
            'model': self.model
        }
class Smart(View):
    def get(self, request:HttpRequest,pk:int =None):
            if pk:
               smart = Smartphones.objects.get(id =pk) 
               return JsonResponse(to_dict(smart))
            else:
                smart = Smartphones.objects.all()
                data = [] 
                for i in smart:
                    data.append( to_dict(i))
                return JsonResponse(data,safe=False)
    def post(self,request:HttpRequest):
            body = request.body.decode("utf-8")
            data = json.loads(body)
            name = data.get("name",False)
            img_url = data.get("img_url",False)
            color = data.get("color",False)
            ram = data.get("ram",False)
            memory = data.get("memory",False)
            price = data.get("price",False)
            model = data.get("model",False)
            
            if price == False:
                return JsonResponse({'status':'price not found'})
            if img_url == False:
                return JsonResponse({'status':'img not found'})
            if color == False:
                return JsonResponse({'status':'color not found'})
            if ram == False:
                return JsonResponse({'status':'ram not found'})
            if memory == False:
                return JsonResponse({'status':'memory not found'})
            if name == False:
                return JsonResponse({'status':' name not found'})
            if model == False:
                return JsonResponse({'status':'model not found'})
            
            yil = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
            a = random.choice(yil)
            dat = a
            Smartphones.objects.create(
                price = price,
                img_url = img_url,
                color = color,
                ram = ram,
                memory = memory,
                name = name,
                model = model,
                release_date = dat  
            )
            return JsonResponse(data)
    def delete(self,request,pk):
        if pk:
            smart = Smartphones.object.get(id=pk)
            smart.delete()
            return JsonResponse({"response":"O'chirildi!"})
        else:
            return JsonResponse({"status":"pk kiriting"})
    def update(self, request,pk):
        if pk:
            smart = Smartphones.objects.get(id=pk)
            a = json.loads(request.body.decode("utf-8"))
            smart.price = a.get('price',smart.price)
            smart.img_url= a.get('img_url',smart.img_url)
            smart.color = a.get('color',smart.color)
            smart.ram = a.get("ram",smart.ram)
            smart.memory = a.get("memory",smart.memory)
            smart.name = a.get("name",smart.name)
            smart.model = a.get("model",smart.model)
            smart.release_date = a.get("release_date",smart.release_date)
            smart.save()
            return JsonResponse({"message": "Updated"})         
        else:
            return JsonResponse({"status":"pk kiriting"})