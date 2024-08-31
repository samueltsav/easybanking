import uuid

class Customer:
    def __init__(self, req_id, description):
        self.req_id = req_id
        self. description = description

    def list_customer_service_requests():
        for req_id, description in Customer.customer_service_requests.items():
            print(f"Request ID: {req_id}, Description: {description}")

    def create_customer_service_request(description):
        request_id = str(uuid.uuid4())
        Customer.customer_service_requests[request_id] = description
        return request_id