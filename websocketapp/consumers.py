from .models import Student,Address
from .serializers import StudentSerializer,AddressSerializer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
import json
import time

class StudentConsumer(GenericAsyncAPIConsumer):
# class StudentConsumer(ListModelMixin,GenericAsyncAPIConsumer):

    # queryset = Student.objects.all()
    

    async def connect(self,**kwargs):
        await self.model_change.subscribe()
        # await self.model_change1.subscribe()
        await super().connect()

        # await self.send_json({"Connection":"Connected"})

    @model_observer(Student)
    async def model_change(self,message,observer=None,**kwargs):
        await self.send_json(message)
    
    # @model_observer(Address)
    # async def model_change1(self,message,observer=None,**kwargs):
    #     await self.send_json(message)

    @model_change.serializer
    def model_serializer(self,instance,action,**kwargs):
        return dict(data = StudentSerializer(instance=instance).data,action=action.value)
    
    # @model_change1.serializer
    # def model_serializer1(self,instance,action,**kwargs):
    #     return dict(data = AddressSerializer(instance=instance).data,action=action.value)