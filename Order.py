class order:

    Date = ''
    Status = ''
    ShoppingCart = ''
    DeliveryAddress = ''
    PaymentMethod = ''

    def validatePayment(self):
        print("Validating payment...")
        self.Status = "Payment Validated"

    def cancel(self):
        print("Cancelling order...")
        self.Status = "Cancelled"

    def dispatch(self):
        print("Dispatching order...")
        self.Status = "Dispatched"

    def confirmDelivery(self):
        print("Confirming delivery...")
        self.Status = "Delivered"

    def refund(self):
        print("Refunding order...")
        self.Status = "Refunded"

    def archive(self):
        print("Archiving order...")
        self.Status = "Archived"