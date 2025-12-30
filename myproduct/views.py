from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myproduct.models import Myproduct
from drf_yasg.utils import swagger_auto_schema
from myproduct.serializers import MyproductSerializer



@swagger_auto_schema(method='get', responses={200: MyproductSerializer(many=True)})
@swagger_auto_schema(method='post', request_body= MyproductSerializer)

@api_view(["GET", "POST"])
def myproduct_list(request):
    
    #Since this view allows multiple HTTP methods, we must check which method to use
    if request.method == "GET":
        snippets = Myproduct.objects.all() #get data from database
        serializer = MyproductSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MyproductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=MyproductSerializer)
@swagger_auto_schema(method='delete', responses={204: 'Deleted'})   

#we do these methods for single data so we do differently
@api_view(["PUT", "DELETE"])
def myproduct_detail(request, pk):
    
    try:
        snippet = Myproduct.objects.get(pk=pk)
    except Myproduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = MyproductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


