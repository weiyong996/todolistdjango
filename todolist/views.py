import logging

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from todolist.serializers import ItemSerializer
from todolist.models import Item


class ItemListView(APIView):
    """
    获取所有Item
    创建1个新Item
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        items = Item.objects.all()
        # 序列化（从库中获取数据），items表示要序列化的对象，many=True表示items是多个对象的实例
        # 如果items只有1个对象实例，则不需要many=True
        serializer = ItemSerializer(items, many=True)
        return Response({'status': True, 'message': '成功', 'data': serializer.data})

    def post(self, request):
        print(request.data.get('content1', 'x'))
        # 反序列化（创建，将数据写入库中），加data参数，表示将data的值写入库中
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logging.info(f"data: {serializer.data}")
            return Response(serializer.data)
        return Response({'status': False, 'message': '失败'})


class ItemDetailView(APIView):
    """
    检索、更新或删除一个Item
    """

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response({'status': True, 'message': '成功', 'data': serializer.data})

    def put(self, request, pk):
        item = self.get_object(pk)
        # 反序列化（更新），需要提供两个参数item
        # 第一个参数item表示需要更新的实例，第二个参数data表示item的新值
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': '成功', 'data': serializer.data})
        return Response({'status': False, 'message': '失败'})

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response({'status': True, 'message': '成功'})
