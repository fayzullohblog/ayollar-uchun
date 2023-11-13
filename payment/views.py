from django.shortcuts import get_object_or_404
from .serializer import OrderSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Order
from courses.models import Course
from environ import Env

env = Env()
env.read_env()

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_object(self):
        order_id = self.kwargs.get("pk")
        obj = get_object_or_404(self.queryset, order_id=order_id)
        return obj


#PAYMENT Views

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CardInformationSerializer
from stripe.error import StripeError
import stripe

class PaymentAPI(APIView):
    serializer_class = CardInformationSerializer

    def post(self, request, course_id):
        serializer = self.serializer_class(data=request.data)
        response = {}

        if serializer.is_valid():
            data_dict = serializer.data

            # Retrieve the Course based on the course_id
            try:
                course = Course.objects.get(id=course_id)
                price = course.price  # Get the price from the Course object
            except Course.DoesNotExist:
                return Response({'detail': 'Course not found.'}, status=status.HTTP_NOT_FOUND)

            stripe.api_key = env.str("STRIPE_SECRET_KEY")
            response = self.stripe_card_payment(data_dict=data_dict, price=price)

            if response.get('status') == status.HTTP_200_OK:
                # Payment was successful, update the 'paid' field in the Order model
                order, created = Order.objects.get_or_create(user=request.user, course=course)
                order.paid = True
                order.save()

        else:
            response = {'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST}

        return Response(response)

    def stripe_card_payment(self, data_dict,price):
        try:
            card_details = {
                "type": "card",
                "card": {
                    "number": data_dict['card_number'],
                    "exp_month": data_dict['expiry_month'],
                    "exp_year": data_dict['expiry_year'],
                    "cvc": data_dict['cvc'],
                }
            }

            payment_intent = stripe.PaymentIntent.create(
                amount=price * 100,
                currency='usd',
                payment_method_types=['card'],
            )

            payment_intent_modified = stripe.PaymentIntent.modify(
                payment_intent['id'],
                payment_method=card_details['id'],
            )

            try:
                payment_confirm = stripe.PaymentIntent.confirm(
                    payment_intent['id']
                )
                payment_intent_modified = stripe.PaymentIntent.retrieve(payment_intent['id'])

            except StripeError as e:
                payment_intent_modified = stripe.PaymentIntent.retrieve(payment_intent['id'])
                payment_confirm = {
                    "stripe_payment_error": "Failed",
                    "code": e.code,
                    "message": e.user_message,
                    'status': "Failed"
                }

            if payment_intent_modified.status == 'succeeded':
                response = {
                    'message': "Card Payment Success",
                    'status': status.HTTP_200_OK,
                    "card_details": card_details,
                    "payment_intent": payment_intent_modified,
                    "payment_confirm": payment_confirm
                }
            else:
                response = {
                    'message': "Card Payment Failed",
                    'status': status.HTTP_400_BAD_REQUEST,
                    "card_details": card_details,
                    "payment_intent": payment_intent_modified,
                    "payment_confirm": payment_confirm
                }
        except StripeError as e:
            response = {
                'error': str(e),
                'status': status.HTTP_400_BAD_REQUEST,
                "payment_intent": {"id": "Null"},
                "payment_confirm": {'status': "Failed"}
            }

        return response
