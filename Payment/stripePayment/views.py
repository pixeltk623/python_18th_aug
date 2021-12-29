from django.http import HttpResponse
import stripe
from django.shortcuts import render



def paymentForm(request):
	return render(request, 'payment.html')

def chargePayment(request):
	stripe.api_key = "sk_test_4NBbDxxVc50ogIZOEARYRKNP00AnsXYzDi"
	token = request.POST['stripeToken']
	amount = request.POST['amount']

	print(amount)

	p = stripe.Charge.create(
	  amount=int(amount)*100,
	  currency="inr",
	  source=token,
	  description="Meet Payment",
	)
	return HttpResponse("Payment Done")


def index(request):
	# SECRET_KEY = env('Secret_key')
	# print(SECRET_KEY)
	stripe.api_key = "sk_test_4NBbDxxVc50ogIZOEARYRKNP00AnsXYzDi"

	# r = stripe.PaymentMethod.create(
	#   type="card",
	#   card={
	#     "number": "4242424242424242",
	#     "exp_month": 12,
	#     "exp_year": 2022,
	#     "cvc": "314",
	#   },
	# )


	# p = stripe.Charge.create(
	#   amount=2000,
	#   currency="inr",
	#   source="tok_visa",
	#   description="Meet Payment",
	# )

	# c = stripe.Customer.list(limit=3)
	# c = stripe.Customer.create(
	#   description="Vadodara Users",
	#   name = "Meet"
	# )

	# re = stripe.Refund.create(
	#   charge="ch_1KC1lzAyRbhKDr5DdxxVDnzN",
	# )
	print(stripe.BalanceTransaction.list(limit=3))
	return HttpResponse("Hello, world. You're at the polls index.")