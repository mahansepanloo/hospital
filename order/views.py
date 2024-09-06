from rest_framework import generics, status
from rest_framework.response import Response
from .models import Orders
from .serializers import OrdersSerializer
from Services.models import Service
from accounts.models import Bimar
from Services.permission import IsNurse
from django.core.exceptions import ValidationError

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsNurse]

    def create(self, request, *args, **kwargs):
        bimar_id = request.data.get('bimar_id')
        service_id = request.data.get('service_id')
        price = request.data.get('price')

        try:
            bimar_instance = Bimar.objects.get(id=bimar_id)
            service_instance = Service.objects.get(id=service_id)

            order_data = {
                'bimar': bimar_instance.id,
                'service': service_instance.id,
                'price': price
            }

            serializer = self.get_serializer(data=order_data)
            serializer.is_valid(raise_exception=True)
            order = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Bimar.DoesNotExist:
            return Response({"error": "Bimar not found."}, status=status.HTTP_404_NOT_FOUND)
        except Service.DoesNotExist:
            return Response({"error": "Service not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)