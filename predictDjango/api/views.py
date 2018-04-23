from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from predictDjango.predictors import predict
from .serializers import InputSerializer

class PredictApi(APIView):
    def post(self, request):
        serializer = InputSerializer(data=request.data)

        if serializer.is_valid():
            input = serializer.data['input']
            answer = predict(input)
            return Response({'answer': answer})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_40HTTP_400_BAD_REQUEST)
